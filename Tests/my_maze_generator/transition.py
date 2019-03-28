from print_maze import *
import copy

class Transiction:

    def __init__(self, oldMaze, newMaze, startCell):
        self.num_cells_x = oldMaze.num_cells_x
        self.num_cells_y = oldMaze.num_cells_y
        self.startCell = startCell
        self.mazesMatrices = [oldMaze.matrix]

        width = self.num_cells_x * 2 + 1
        height = self.num_cells_y * 2 + 1

        x = self.startCell[0] * 2 + 1
        y = self.startCell[1] * 2 + 1

        M = copy.deepcopy(oldMaze.matrix)
        j = 1
        while x - j >= 0 or x + j <= width or y - j >= 0 or y + j <= height:
            x_min, y_min = max(0, x - j), max(0, y - j)
            x_max, y_max = min(width, x + j), min(height, y + j)

            M[y_min: y_max, x_min] = copy.deepcopy(newMaze.matrix[y_min: y_max, x_min])
            M[y_min: y_max, x_max - 1] = copy.deepcopy(newMaze.matrix[y_min: y_max, x_max - 1])
            M[y_min, x_min:x_max] = copy.deepcopy(newMaze.matrix[y_min, x_min:x_max])
            M[y_max - 1, x_min:x_max] = copy.deepcopy(newMaze.matrix[y_max - 1, x_min:x_max])

            self.mazesMatrices.append(copy.deepcopy(M))
            j += 1


