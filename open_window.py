import pygame

class Window:

    font_location = "fonts/conthrax-sb.ttf"

    def __init__(self, size, background):
        self.size = size
        self.background = background
        pygame.init()
        self.window = pygame.display.set_mode(self.size)

    def showText(self, text, position, font_size):
        title_font = pygame.font.Font(self.font_location,font_size)
        text_surface = title_font.render(text, True, (0,0,0))
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = position
        self.window.blit(text_surface, text_rectangle)

    def showImage(self, image_path, position, scale):
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, scale)
        self.window.blit(image, position)

    def openWindow(self):
        pygame.display.set_caption("Crazy Maze")
        background_image = pygame.image.load(self.background)
        background_image = pygame.transform.scale(background_image, self.size)
        game_loop = True
        while game_loop:

            for event in pygame.event.get():

                if (event.type == pygame.QUIT):
                    game_loop = False

            self.window.blit(background_image, (0,0))
            self.showText("Crazy Maze", (self.size[0]/2, self.size[1]/2), 120)
            pygame.display.flip()

        pygame.quit()





