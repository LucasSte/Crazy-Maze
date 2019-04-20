import pygame
from open_window import Window
from open_window import Action
from algorithm import AuxFunc
import numpy as np


class Character(pygame.sprite.Sprite, Window):

    def __init__(self, lives, window, start_position=(1, 1)):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.frame = 0
        self.size = (int(window.pxl_x-1), int(window.pxl_y))

        for i in range(1, 4):
            image_aux = pygame.image.load('images/Walk(' + str(i) + ').png')
            image_aux = pygame.transform.scale(image_aux, self.size)
            self.images.append(image_aux)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

        self.rect.x = int(start_position[0]*window.pxl_x) +1
        self.rect.y = int(start_position[1]*window.pxl_y) +1
        self.lives = lives
        self.window = window

    def getCharacterNode(self, maze):  # of your center

        matrix_shape = maze.matrix.shape

        player_matrix_x = int((self.rect.x+self.window.pxl_x/2)*matrix_shape[1]/Window.size[0])
        player_matrix_y = int((self.rect.y+self.window.pxl_y/2)*matrix_shape[0]/Window.size[1])

        player_node = (player_matrix_y, player_matrix_x)

        return player_node

    def rectDownRight(self):
        pos = (self.rect.x + self.size[0], self.rect.y + self.size[1])
        return pos


    def control(self, y, x, maze):

        downRightPos = self.rectDownRight()
        max_pos_x = downRightPos[0] + 4*x -7# o -7 eh para dar uma folga no seu cabelo da frente
        min_pos_x = self.rect.x + 4*x +7  # o +7 eh para dar uma folga nas suas costas
        max_pos_y = downRightPos[1] + 4 * y
        min_pos_y = self.rect.y + 4 * y +15  ## o +15 eh para dar uma folga no seu cabelo

        if x > 0:
            desired_pos1 = (max_pos_x, min_pos_y)
            desired_pos2 = (max_pos_x, max_pos_y)
        elif x < 0:
            desired_pos1 = (min_pos_x, min_pos_y)
            desired_pos2 = (min_pos_x, max_pos_y)
        elif y > 0:
            desired_pos1 = (min_pos_x, max_pos_y)
            desired_pos2 = (max_pos_x, max_pos_y)
        elif y < 0:
            desired_pos1 = (min_pos_x, min_pos_y)
            desired_pos2 = (max_pos_x, min_pos_y)

        desired_node1 = AuxFunc.getNode(desired_pos1[0], desired_pos1[1], maze, self.window)
        desired_node2 = AuxFunc.getNode(desired_pos2[0], desired_pos2[1], maze, self.window)

        if maze.matrix[desired_node1[0]][desired_node1[1]] == 0 and \
                maze.matrix[desired_node2[0]][desired_node2[1]] == 0:  # if is grass (path)
            self.rect.x += 4*x
            self.rect.y += 4*y
            if x > 0 or y > 0:
                self.frame += 1
                self.frame = self.frame % 3
                self.image = self.images[self.frame]
            elif x < 0 or y < 0:
                self.frame -= 1
                if self.frame < 0:
                    self.frame = 2
                self.image = self.images[self.frame]

    def updateLives(self, number):
        self.lives += number

        if self.lives == 0:
            return Action.player_dead
        else:
            return Action.stand_by

    def detectMonsterCollision(self, monster_1, monster_2, monster_3, maze):
        monster_1_distance = np.sqrt((monster_1.rect.x - self.rect.x)**2 + (monster_1.rect.y - self.rect.y)**2)
        monster_2_distance = np.sqrt((monster_2.rect.x - self.rect.x)**2 + (monster_2.rect.y - self.rect.y)**2)
        monster_3_distance = np.sqrt((monster_3.rect.x - self.rect.x)**2 + (monster_3.rect.y - self.rect.y)**2)

        if monster_1_distance < 32:
            self.rect.x += 1
            self.rect.y += 1

            monster_1.resetPosition()
            monster_1.findNewPosition(self, maze)

            return self.updateLives(-1)

        elif monster_2_distance < 32:
            self.rect.x += 1
            self.rect.y += 1

            monster_2.resetPosition()
            monster_2.findNewPosition(self, maze)

            return self.updateLives(-1)

        elif monster_3_distance < 32:
            self.rect.x += 1
            self.rect.y += 1

            monster_3.resetPosition()
            monster_3.findNewPosition(self, maze)

            return self.updateLives(-1)

        else:
            return Action.stand_by

    def detectWin(self, maze, action_local):
        postition = self.getCharacterNode(maze)

        # winning has preference
        if postition[1] == maze.width - 2 and postition[0] == maze.height - 2:
            return Action.player_win

        return action_local
