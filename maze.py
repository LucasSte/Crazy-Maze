import numpy as np
import copy
from algorithm import Algorithm


# Usa o algoritmo de Prim, logo o labirinto é um conjunto de celulas conexas
# (o jogador pode chegar em qualquer celula partindo de qualquer celula)

# IMPORTANTE: Para que o labirinto seja dinamico, o jogador nao deve
#             ocupar uma poscao que antes era de uma parede, apenas posicao de celulas


class Maze:

    def __init__(self, maze_shape, start_node=(0, 0)):
        self.num_nodes_x = maze_shape[0]
        self.num_nodes_y = maze_shape[1]
        self.start_node = start_node

        self.width = maze_shape[0] * 2 + 1
        self.height = maze_shape[1] * 2 + 1

        # Transition variable:
        self.update_counter = 0
        self.delay_counter = 0
        self.max_delay_counter = 50
        self.mazes_matrices = []

        self.matrix = Algorithm.prim(self)

    def newTrasition(self, player_cell):
        self.update_counter = 0
        self.mazes_matrices = [self.matrix]

        start_node = (int((player_cell[0]-1)/2), int((player_cell[1]-1)/2))
        new_maze = Maze((self.num_nodes_x, self.num_nodes_y), start_node)

        x = start_node[0]
        y = start_node[1]

        M = copy.deepcopy(self.matrix)
        j = 1
        while x - j >= 0 or x + j <= self.width or y - j >= 0 or y + j <= self.height:
            x_min, y_min = max(0, x - j), max(0, y - j)
            x_max, y_max = min(self.width, x + j), min(self.height, y + j)

            M[x_min, y_min: y_max] = copy.deepcopy(new_maze.matrix[x_min, y_min: y_max])
            M[x_max - 1, y_min: y_max] = copy.deepcopy(new_maze.matrix[x_max - 1, y_min: y_max])
            M[x_min:x_max, y_min] = copy.deepcopy(new_maze.matrix[x_min:x_max, y_min])
            M[x_min:x_max, y_max - 1] = copy.deepcopy(new_maze.matrix[x_min:x_max, y_max - 1])

            self.mazes_matrices.append(copy.deepcopy(M))
            j += 1

    def updateMaze(self, player_cell):

        if self.delay_counter == self.max_delay_counter:
            if self.update_counter == 0 or self.update_counter >= len(self.mazes_matrices)-1:
                self.newTrasition(player_cell)

            self.update_counter = self.update_counter + 1
            self.matrix = self.mazes_matrices[self.update_counter]
            self.delay_counter = 0

        else:
            self.delay_counter = self.delay_counter+1
