import pygame
from open_window import Window
from algorithm import Algorithm
from algorithm import AuxFunc
from enum import Enum
from global_variables import Global_variables


class Move(Enum):
    up = 1
    left = 2
    down = 3
    right = 4


class Monster(Window, pygame.sprite.Sprite):

    path_to_player = list()
    last_monster_cell_x = -1
    last_monster_cell_y = -1
    aStar_delay = 20
    aStar_counter = 0
    last_movement = 0

    def __init__(self, image_path, cell, speed):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.size = (25, 25)
        self.frame = 0
        image_aux = pygame.image.load(image_path)
        image_aux = pygame.transform.scale(image_aux, self.size)
        self.image = image_aux
        self.rect = self.image.get_rect()
        start_position_x = cell[0]*Global_variables.cell_size_x + 1
        start_position_y = cell[1]*Global_variables.cell_size_y + 1
        self.start_position = (start_position_x, start_position_y)
        self.rect.x = start_position_x
        self.rect.y = start_position_y
        self.speed = speed

    def resetPosition(self):
        self.rect.x = self.start_position[0]
        self.rect.y = self.start_position[1]

    def getMonsterNode(self, maze): # of your center

        matrix_shape = maze.matrix.shape

        monster_matrix_x = int((self.rect.x+self.size[0]/2)*matrix_shape[1]/Global_variables.window_size[0])
        monster_matrix_y = int((self.rect.y+self.size[1]/2)*matrix_shape[0]/Global_variables.window_size[1])

        monster_cell = (monster_matrix_y, monster_matrix_x)

        return monster_cell

    def findNewPath(self, player, maze, window):

        # aStar eh muito pesado e estava causando lag no jogo, adicionei um delay para sua execucao:
        if self.aStar_counter == 0 or self.aStar_counter > self.aStar_delay:
<<<<<<< Updated upstream
            player_node = player.getCharacterNode(maze, window)
            monster_node = self.getMonsterNode(maze)
            if maze.matrix[player_node[0]][player_node[1]] == 0:
                if self.last_monster_node_x != monster_node[0] or self.last_monster_node_y != monster_node[1]:
                    self.path_to_player = Algorithm.aStar(maze.matrix, monster_node, player_node)
=======
            player_cell = player.getCharacterNode(maze)
            monster_cell = self.getMonsterNode(maze)
            if maze.matrix[player_cell[0]][player_cell[1]] == 0:
                if self.last_monster_cell_x != monster_cell[0] or self.last_monster_cell_y != monster_cell[1]:
                    self.path_to_player = Algorithm.aStar(maze.matrix, monster_cell, player_cell)
>>>>>>> Stashed changes

            self.aStar_counter = 0

        self.aStar_counter = self.aStar_counter + 1


    def inOnlyOneNode(self, maze):
        up_left_corner = AuxFunc.getCell(self.rect.x, self.rect.y, maze)
        up_right_corner = AuxFunc.getCell(self.rect.x+self.size[0], self.rect.y, maze)

        if up_left_corner[0] != up_right_corner[0] or up_left_corner[1] != up_right_corner[1]:
            return False
        down_left_corner = AuxFunc.getCell(self.rect.x, self.rect.y + self.size[1], maze)
        if up_left_corner[0] != down_left_corner[0] or up_left_corner[1] != down_left_corner[1]:
            return False
        down_right_corner = AuxFunc.getCell(self.rect.x + self.size[0], self.rect.y+self.size[1], maze)
        if up_left_corner[0] != down_right_corner[0] or up_left_corner[1] != down_right_corner[1]:
            return False
        else:
            return True

    def updatePosition(self, maze):
        if self.path_to_player is not None and len(self.path_to_player) > 0:
            next_cell = self.path_to_player[-1]
            # monster's current position:
            up_left_corner = AuxFunc.getCell(self.rect.x, self.rect.y, maze)
            down_right_corner = AuxFunc.getCell(self.rect.x + self.size[0], self.rect.y + self.size[1], maze)

            if down_right_corner[0] - next_cell[0] > 0:
                self.rect.y -= self.speed
            elif up_left_corner[0] - next_cell[0] < 0:
                self.rect.y += self.speed
            elif down_right_corner[1] - next_cell[1] > 0:
                self.rect.x -= self.speed
            elif up_left_corner[1] - next_cell[1] < 0:
                self.rect.x += self.speed
            else:
                self.path_to_player.pop()

            # if self.inOnlyOneNode(maze, window):
            #     # print("in only")
            #     if down_right_corner[0] - next_cell[0] > 0:
            #         self.rect.y -= self.speed
            #         self.last_movement = Move.up
            #     elif up_left_corner[0] - next_cell[0] < 0:
            #         self.rect.y += self.speed
            #         self.last_movement = Move.down
            #     elif down_right_corner[1] - next_cell[1] > 0:
            #         self.rect.x -= self.speed
            #         self.last_movement = Move.left
            #     elif up_left_corner[1] - next_cell[1] < 0:
            #         self.rect.x += self.speed
            #         self.last_movement = Move.right
            #     else:
            #         self.updateNextNode(window)
            # else:
            #     # print("not in only")
            #     if self.last_movement == Move.up:
            #         self.rect.y -= self.speed
            #     elif self.last_movement == Move.down:
            #         self.rect.y += self.speed
            #     elif self.last_movement == Move.left:
            #         self.rect.x -= self.speed
            #     elif self.last_movement == Move.right:
            #         self.rect.x += self.speed
