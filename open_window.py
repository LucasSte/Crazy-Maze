import pygame

class Window:

    def __init__(self, size, background):
        self.size = size
        self.background = background

    def OpenWindow(self):
        pygame.init()
        window = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Crazy Maze")
        background_image = pygame.image.load(self.background)
        background_image = pygame.transform.scale(background_image, self.size)
        game_loop = True
        while game_loop:

            for event in pygame.event.get():

                if (event.type == pygame.QUIT):
                    game_loop = False

            window.blit(background_image, (0,0))
            pygame.display.flip()

        pygame.quit()


