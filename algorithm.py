import numpy as np
from numpy.random import randint as rand
from open_window import  Window
from heapq import *


class Node:
    # node class for A* Pathfinding

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


class Algorithm:

    @staticmethod
    def prim(maze):

        matrix = np.array(
            [[1] * maze.width, [1, 0] * maze.num_cells_x + [1]] * maze.num_cells_y + [[1] * maze.width], dtype=int)

        visited = np.zeros([maze.num_cells_y, maze.num_cells_x], dtype=bool)

        # Mark the cell as visited and add to set
        visited[maze.start_cell[1], maze.start_cell[0]] = 1
        path = [maze.start_cell]

        # While the set of cells is not empty
        while len(path):

            # Select randomly a cell to extend the path and remove it from the set
            (cell_x, cell_y) = path[rand(0, len(path))]

            # Get available neighbours
            neighbours = []
            if cell_x > 0 and not visited[cell_y, cell_x - 1]:
                neighbours.append([cell_x - 1, cell_y])

            if cell_x < maze.num_cells_x - 1 and not visited[cell_y, cell_x + 1]:
                neighbours.append([cell_x + 1, cell_y])

            if cell_y > 0 and not visited[cell_y - 1, cell_x]:
                neighbours.append([cell_x, cell_y - 1])

            if cell_y < maze.num_cells_y - 1 and not visited[cell_y + 1, cell_x]:
                neighbours.append([cell_x, cell_y + 1])

            # Remove the cell if it does not lead anywhere
            if len(neighbours) == 0:
                path.remove((cell_x, cell_y))

            else:
                # Randomly connect to an available cell
                [cX, cY] = neighbours[rand(0, len(neighbours))]
                visited[cY, cX] = 1
                path.append((cX, cY))
                # Removes the wall between them
                matrix[(cY + cell_y + 1), (cX + cell_x + 1)] = 0

        return matrix

    @staticmethod
    def aStar(array, start, goal):

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        close_set = set()
        came_from = {}
        gscore = {start: 0}
        fscore = {start: AuxFunc.heuristic(start, goal)}
        oheap = []

        heappush(oheap, (fscore[start], start))

        while oheap:

            current = heappop(oheap)[1]

            if current == goal:
                data = []
                while current in came_from:
                    data.append(current)
                    current = came_from[current]
                return data

            close_set.add(current)
            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j
                tentative_g_score = gscore[current] + AuxFunc.heuristic(current, neighbor)
                if 0 <= neighbor[0] < array.shape[0]:
                    if 0 <= neighbor[1] < array.shape[1]:
                        if array[neighbor[0]][neighbor[1]] == 1:
                            continue
                    else:
                        # array bound y walls
                        continue
                else:
                    # array bound x walls
                    continue

                if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                    continue

                if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + AuxFunc.heuristic(neighbor, goal)
                    heappush(oheap, (fscore[neighbor], neighbor))

        return None


class AuxFunc(Window):

    @staticmethod
    def getNode(position_x, position_y, maze):

        matrix_shape = maze.matrix.shape

        character_matrix_x = int(position_x*matrix_shape[1]/Window.size[0])
        character_matrix_y = int(position_y*matrix_shape[0]/Window.size[1])

        character_node = (character_matrix_y, character_matrix_x)

        return character_node

    @staticmethod
    def heuristic(a, b):
        return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
