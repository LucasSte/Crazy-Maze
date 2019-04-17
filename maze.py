import numpy as np
from numpy.random import randint as rand
import copy


# Usa o algoritmo de Prim, logo o labirinto é um conjunto de celulas conexas
# (o jogador pode chegar em qualquer celula partindo de qualquer celula)

# IMPORTANTE: Para que o labirinto seja dinamico, o jogador nao deve
#             ocupar uma poscao que antes era de uma parede, apenas posicao de celulas

# Ao longo do codigo tem-se usado a seguinte padroniacao:
#   - cell = noh do grafo
#   - node = posicao na matriz que descreve o labirinto
## sim, eh uma notacao confusa e deve ser ajeitada


class Maze:

    def __init__(self, num_cells_x, num_cells_y, start_cell=(0, 0)):
        self.num_cells_x = num_cells_x
        self.num_cells_y = num_cells_y
        self.start_cell = start_cell

        self.width = self.num_cells_x * 2 + 1
        self.height = self.num_cells_y * 2 + 1

        self.update_counter = 0
        self.update_delay = 0
        self.max_delay = 5
        self.mazes_matrices = []

        visited = np.zeros([self.num_cells_y, self.num_cells_x], dtype=bool)
        self.matrix = np.array([[1] * self.width, [1, 0] * self.num_cells_x + [1]] * self.num_cells_y + [[1] * self.width], dtype=int)


        # Mark the cell as visited and add to set
        visited[self.start_cell[1], self.start_cell[0]] = 1
        path = [self.start_cell]

        # While the set of cells is not empty
        while len(path):

            # Select randomly a cell to extend the path and remove it from the set
            (cell_x, cell_y) = path[rand(0, len(path))]

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
                path.remove((cell_x, cell_y))

            else:
                # Randomly connect to an available cell
                [cX, cY] = neighbours[rand(0, len(neighbours))]
                visited[cY, cX] = 1
                path.append((cX, cY))
                # Removes the wall between them
                self.matrix[(cY + cell_y + 1), (cX + cell_x + 1)] = 0

    def newTrasition(self, player):
        self.update_counter = 0
        self.mazes_matrices = [self.matrix]

        start_node = player.getNode(self)
        start_cell = (int((start_node[0]-1)/2), int((start_node[1]-1)/2))
        new_maze = Maze(self.num_cells_x, self.num_cells_y, start_cell)

        x = start_node[0]
        y = start_node[1]

        M = copy.deepcopy(self.matrix)
        j = 1
        while x - j >= 0 or x + j <= self.width or y - j >= 0 or y + j <= self.height:
            x_min, y_min = max(0, x - j), max(0, y - j)
            x_max, y_max = min(self.width, x + j), min(self.height, y + j)

            M[y_min: y_max, x_min] = copy.deepcopy(new_maze.matrix[y_min: y_max, x_min])
            M[y_min: y_max, x_max - 1] = copy.deepcopy(new_maze.matrix[y_min: y_max, x_max - 1])
            M[y_min, x_min:x_max] = copy.deepcopy(new_maze.matrix[y_min, x_min:x_max])
            M[y_max - 1, x_min:x_max] = copy.deepcopy(new_maze.matrix[y_max - 1, x_min:x_max])

            self.mazes_matrices.append(copy.deepcopy(M))
            j += 1

    def updateMaze(self, player):

        if self.update_delay == self.max_delay:
            if self.update_counter == 0 or self.update_counter >= len(self.mazes_matrices)-1:
                self.newTrasition(player)

            self.update_counter = self.update_counter + 1
            self.matrix = self.mazes_matrices[self.update_counter]
            self.update_delay = 0

        else:
            self.update_delay = self.update_delay+1