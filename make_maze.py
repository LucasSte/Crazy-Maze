import numpy as np
from numpy.random import randint as rand

# Usa o algoritmo de Prim, logo o labirinto é um conjunto de celulas conexas
# (o jogador pode chegar em qualquer celula partindo de qualquer celula)

# IMPORTANTE: Para que o labirinto seja dinamico, o jogador nao deve
#             ocupar uma poscao que antes era de uma parede, apenas posicao de celulas


class Maze:

    def __init__(self, num_cells_x, num_cells_y, startCell=[0, 0]):
        self.num_cells_x = num_cells_x
        self.num_cells_y = num_cells_y
        self.dynamize(startCell)

    def dynamize(self, startCell = [0,0] ):
        self.startCell = startCell

        width = self.num_cells_x * 2 + 1
        height = self.num_cells_y * 2 + 1

        visited = np.zeros([self.num_cells_y, self.num_cells_x], dtype=bool)
        self.matrix = np.array([[1] * width, [1, 0] * self.num_cells_x + [1]] * self.num_cells_y + [[1] * width])

        # Mark the cell as visited and add to set
        visited[self.startCell[1], self.startCell[0]] = 1
        path = [self.startCell]

        # While the set of cells is not empty
        while len(path):

            # Select randomly a cell to extend the path and remove it from the set
            [cell_x, cell_y] = path[rand(0, len(path))]

            # Get available neighbours
            neighbours = []
            if cell_x > 0 and not visited[cell_y, cell_x - 1]:
                neighbours.append([cell_x - 1, cell_y])

            if cell_x < self.num_cells_x - 1 and not visited[cell_y, cell_x + 1]:
                neighbours.append([cell_x + 1, cell_y])

            if cell_y > 0 and not visited[cell_y - 1, cell_x]:
                neighbours.append([cell_x, cell_y - 1])

            if cell_y < self.num_cells_y - 1 and not visited[cell_y + 1, cell_x]:
                neighbours.append([cell_x, cell_y + 1])

            # Remove the cell if it does not lead anywhere
            if len(neighbours) == 0:
                path.remove([cell_x, cell_y])

            else:
                # Randomly connect to an available cell
                [cX, cY] = neighbours[rand(0, len(neighbours))]
                visited[cY, cX] = 1
                path.append([cX, cY])
                # Removes the wall between them
                self.matrix[(cY + cell_y + 1), (cX + cell_x + 1)] = 0
