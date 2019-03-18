import pygame
from open_window import Window


class Character(pygame.sprite.Sprite, Window):

    def __init__(self, start_position_x, start_position_y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.restrictions = Window.size ##Mudar aqui quando tiver imagem definida
        image_aux = pygame.image.load('images/maze.png')
        self.images.append(image_aux)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = start_position_x
        self.rect.y = start_position_y

    def control(self, y, x):
        if 0 < x + self.rect.x < self.restrictions[0]:
            self.rect.x += x

        if 0 < y + self.rect.y < self.restrictions[1]:
            self.rect.y += y
