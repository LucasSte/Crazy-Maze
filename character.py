import pygame

class Character(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.frame = 0
        self.rect = None

    def getCharacterRectNode(self, game_controller):

        matrix_shape = game_controller.matrix.shape

        matrix_x = int((self.rect.x+game_controller.pxl_x/2)*matrix_shape[1]/game_controller.size[0])
        matrix_y = int((self.rect.y+game_controller.pxl_y/2)*matrix_shape[0]/game_controller.size[1])

        node = (matrix_y, matrix_x)

        return node

    def getNode(self, position_x, position_y, game_controller):

        matrix_shape = game_controller.matrix.shape

        character_matrix_x = int(position_x*matrix_shape[1]/game_controller.size[0])
        character_matrix_y = int(position_y*matrix_shape[0]/game_controller.size[1])

        character_node = (character_matrix_y, character_matrix_x)

        return character_node
