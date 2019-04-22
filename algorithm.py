import numpy as np
from numpy.random import randint as rand
from open_window import Window
from heapq import *
from global_variables import Global_variables

class Algorithm:

    @staticmethod
    def prim(maze):

        matrix = np.array(
            [[1] * maze.width, [1, 0] * maze.num_nodes_x + [1]] * maze.num_nodes_y + [[1] * maze.width], dtype=int)

        matrix = [*zip(*matrix)] # Matrix Transpose (for easy reading | M[x][y] instead of M[y][x])

        visited = np.zeros([maze.num_nodes_x, maze.num_nodes_y], dtype=bool)

        # Mark the node as visited and add to set
        visited[maze.start_node[0], maze.start_node[1]] = 1
        path = [maze.start_node]

        # While the set of nodes is not empty
        while len(path):

            # Select randomly a node to extend the path and remove it from the set
            (node_x, node_y) = path[rand(0, len(path))]

            # Get available neighbours
            neighbours = []
            if node_x > 0 and not visited[node_x - 1, node_y]:
                neighbours.append((node_x - 1, node_y))

            if node_x < maze.num_nodes_x - 1 and not visited[node_x + 1, node_y]:
                neighbours.append((node_x + 1, node_y))

            if node_y > 0 and not visited[node_x, node_y - 1]:
                neighbours.append((node_x, node_y - 1))

            if node_y < maze.num_nodes_y - 1 and not visited[node_x, node_y + 1]:
                neighbours.append((node_x, node_y + 1))

            # Remove the node if it does not lead anywhere
            if len(neighbours) == 0:
                path.remove((node_x, node_y))

            else:
                # Randomly connect to an available node
                [cX, cY] = neighbours[rand(0, len(neighbours))]
                visited[cY, cX] = 1
                path.append((cX, cY))
                # Removes the wall between them
                matrix[(cY + node_y + 1), (cX + node_x + 1)] = 0

        return matrix

    @staticmethod
    def aStar(matrix, start, goal):

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        closed_set = set()
        came_from = {}
        g_score = {start: 0}
        f_score = {start: AuxFunc.heuristic(start, goal)}
        o_heap = []

        heappush(o_heap, (f_score[start], start))

        while o_heap:

            current = heappop(o_heap)[1]

            if current == goal:
                data = []
                while current in came_from:
                    data.append(current)
                    current = came_from[current]
                return data

            closed_set.add(current)
            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j
                tentative_g_score = g_score[current] + AuxFunc.heuristic(current, neighbor)
                if 0 <= neighbor[0] < matrix.shape[0]:
                    if 0 <= neighbor[1] < matrix.shape[1]:
                        if matrix[neighbor[0]][neighbor[1]] == 1:
                            continue
                    else:
                        # array bound y walls
                        continue
                else:
                    # array bound x walls
                    continue

                if neighbor in closed_set and tentative_g_score >= g_score.get(neighbor, 0):
                    continue

                if tentative_g_score < g_score.get(neighbor, 0) or neighbor not in [i[1] for i in o_heap]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + AuxFunc.heuristic(neighbor, goal)
                    heappush(o_heap, (f_score[neighbor], neighbor))

        return None


class AuxFunc(Window):

    @staticmethod
    def getCell(position_x, position_y, maze):

        matrix_shape = maze.matrix.shape

        character_matrix_x = int(position_x*matrix_shape[1]/Global_variables.window_size[0])
        character_matrix_y = int(position_y*matrix_shape[0]/Global_variables.window_size[1])

        character_cell = (character_matrix_y, character_matrix_x)

        return character_cell

    @staticmethod
    def heuristic(a, b):
        return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
