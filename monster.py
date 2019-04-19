import pygame
from open_window import Window
from algorithm import Algorithm
import numpy as np


class Monster(Window, pygame.sprite.Sprite):

    path_to_player = list()
    last_monster_node_x = -1
    last_monster_node_y = -1
    aStar_delay = 20
    aStar_counter = 0

    def __init__(self, image_path, start_position_x, start_position_y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.frame = 0
        image_aux = pygame.image.load(image_path)
        image_aux = pygame.transform.scale(image_aux, (32, 32))
        self.image = image_aux
        self.rect = self.image.get_rect()
        self.start_position = (start_position_x, start_position_y)
        self.rect.x = start_position_x
        self.rect.y = start_position_y
        self.next_position = (start_position_x, start_position_y)
        self.speed = speed

    def resetPosition(self):
        self.rect.x = self.start_position[0]
        self.rect.y = self.start_position[1]

    def getMonsterNode(self, maze):

        matrix_shape = maze.matrix.shape

        monster_matrix_x = int(self.rect.x*matrix_shape[1]/Window.size[0])
        monster_matrix_y = int(self.rect.y*matrix_shape[0]/Window.size[1])

        monster_node = (monster_matrix_y, monster_matrix_x)

        return monster_node

    def findNewPosition(self, player, maze):

        # aStar eh muito pesado e estava causando lag no jogo, adicionei um delay para sua execucao:
        if self.aStar_counter == 0 or self.aStar_counter > self.aStar_delay:
            player_node = player.getCharacterNode(maze)

            monster_node = self.getMonsterNode(maze)

            if self.last_monster_node_x != monster_node[0] or self.last_monster_node_y != monster_node[1]:
                self.path_to_player = Algorithm.aStar(maze.matrix, monster_node, player_node)

            self.aStar_counter = 0

        self.aStar_counter = self.aStar_counter +1


    def getNextPosition(self, window):

        if self.path_to_player is not None and len(self.path_to_player) > 0:
            next_node = self.path_to_player.pop()

            self.next_position = (next_node[0]*window.pxl_y, next_node[1]*window.pxl_x)

    def updatePosition(self, maze, window):


        monster_node = self.getMonsterNode(maze)

        if self.path_to_player is not None and len(self.path_to_player) > 0:
            next_node = self.path_to_player[-1]

            if monster_node[0] - next_node[0] > 0:
                self.rect.y -= self.speed
            elif monster_node[0] - next_node[0] < 0:
                self.rect.y += self.speed
            elif monster_node[1] - next_node[1] > 0:
                self.rect.x -= self.speed
            elif monster_node[1] - next_node[1] < 0:
                self.rect.x += self.speed
            else:
                self.getNextPosition(window)


