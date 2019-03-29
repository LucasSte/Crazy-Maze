import pygame
from open_window import Window


class Character(pygame.sprite.Sprite, Window):

    def __init__(self, start_position_x, start_position_y):
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

    def control(self, y, x, maze, window):

        matrix_shape = maze.matrix.shape

        desired_matrix_x = int((self.rect.x+x)*matrix_shape[1]/Window.size[0])
        desired_matrix_y = int((self.rect.y+y)*matrix_shape[0]/Window.size[1])

        if maze.matrix[desired_matrix_y][desired_matrix_x] == 0:

            if maze.matrix[desired_matrix_y][desired_matrix_x + 1] == 1 and x > 0:
                if x + self.rect.x < desired_matrix_x*window.pxl_y + 15:
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



