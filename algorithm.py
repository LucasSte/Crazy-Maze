import numpy as np
from numpy.random import randint as rand
import copy



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
    def aStar(maze, start, end):

        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end)
        end_node.g = end_node.h = end_node.f = 0

        open_list = []
        closed_list = []

        open_list.append(start_node)

        while len(open_list) > 0:

            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            open_list.pop(current_index)
            closed_list.append(current_node)

            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path

            children = []

            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                if node_position[0] > (len(maze) -1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                    continue

                if maze[node_position[0]][node_position[1]] != 0:
                    continue

                if Node(current_node, node_position) in closed_list:
                    continue

                new_node = Node(current_node, node_position)

                children.append(new_node)

            for child in children:

                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                child.g = current_node.g + 1
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
                child.f = child.g + child.h

                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                open_list.append(child)

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
