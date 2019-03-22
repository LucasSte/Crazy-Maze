import pygame
from open_window import Window


class Character(pygame.sprite.Sprite, Window):

    def __init__(self, start_position_x, start_position_y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.frame = 0
        for i in range(1, 4):
            image_aux = pygame.image.load('images/Walk(' + str(i) + ').png')
            self.images.append(image_aux)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
        self.restrictions = (Window.size[0] - 120, Window.size[1] - 140)
        self.rect.x = start_position_x
        self.rect.y = start_position_y

    def control(self, y, x):
        if 0 < x + self.rect.x < self.restrictions[0]:
            self.rect.x += x

            if x > 0:
                self.frame += 1
                self.frame = self.frame % 2
                self.image = self.images[self.frame]
            elif x < 0:
                self.frame -= 1
                if self.frame < 0:
                    self.frame = 2
                self.image = self.images[self.frame]

        if 0 < y + self.rect.y < self.restrictions[1]:
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
