import pygame
from open_window import Window
from open_window import Action
import numpy as np


class Character(pygame.sprite.Sprite, Window):

    def __init__(self, start_position_x, start_position_y, lives):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.frame = 0
        for i in range(1, 4):
            image_aux = pygame.image.load('images/Walk(' + str(i) + ').png')
            image_aux = pygame.transform.scale(image_aux, (27, 33))
            self.images.append(image_aux)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
        self.rect.x = start_position_x
        self.rect.y = start_position_y
        self.lives = lives

    def getCharacterNode(self, maze):

        matrix_shape = maze.matrix.shape

        player_matrix_x = int(self.rect.x*matrix_shape[1]/Window.size[0])
        player_matrix_y = int(self.rect.y*matrix_shape[0]/Window.size[1])

        player_node = (player_matrix_y, player_matrix_x)

        return player_node

    def control(self, y, x, maze, window):

        matrix_shape = maze.matrix.shape

        desired_matrix_x = int((self.rect.x+x)*matrix_shape[1]/Window.size[0])
        desired_matrix_y = int((self.rect.y+y)*matrix_shape[0]/Window.size[1])

        if maze.matrix[desired_matrix_y][desired_matrix_x] == 0:

            if maze.matrix[desired_matrix_y][desired_matrix_x + 1] == 1 and x > 0:
                if x + self.rect.x < desired_matrix_x*window.pxl_y + 18:
                    self.rect.x += x
                    if x > 0:
                        self.frame += 1
                        self.frame = self.frame % 3
                        self.image = self.images[self.frame]
                    elif x < 0:
                        self.frame -= 1
                        if self.frame < 0:
                            self.frame = 2
                        self.image = self.images[self.frame]
            else:
                self.rect.x += x
                if x > 0:
                    self.frame += 1
                    self.frame = self.frame % 3
                    self.image = self.images[self.frame]
                elif x < 0:
                    self.frame -= 1
                    if self.frame < 0:
                        self.frame = 2
                    self.image = self.images[self.frame]

            if y > 0 and maze.matrix[desired_matrix_y + 1][desired_matrix_x] == 1:

                if not y + self.rect.y > desired_matrix_y*window.pxl_x + 8:
                    self.rect.y += y
                    if y > 0:
                        self.frame += 1
                        self.frame = self.frame % 3
                        self.image = self.images[self.frame]
                    elif y < 0:
                        self.frame -= 1
                        if self.frame < 0:
                            self.frame = 2
                        self.image = self.images[self.frame]

            else:
                self.rect.y += y
                if y > 0:
                    self.frame += 1
                    self.frame = self.frame % 3
                    self.image = self.images[self.frame]
                elif y < 0:
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
