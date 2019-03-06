import pygame

MISSING = object()

class Window:

    font_location = "fonts/conthrax-sb.ttf"

    def __init__(self, size, background):
        self.size = size
        self.background = background
        pygame.init()
        self.window = pygame.display.set_mode(self.size)

    def showText(self, text, position, font_size, color):
        title_font = pygame.font.Font(self.font_location,font_size)
        text_surface = title_font.render(text, True, color)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = position
        self.window.blit(text_surface, text_rectangle)

    def showImage(self, image_path, position, scale=MISSING):
        image = pygame.image.load(image_path)
        if scale is not MISSING:
            image = pygame.transform.scale(image, scale)
        self.window.blit(image, position)

    def openWindow(self):
        pygame.display.set_caption("Crazy Maze")
        background_image = pygame.image.load(self.background)
        background_image = pygame.transform.scale(background_image, self.size)
        self.window.blit(background_image, (0, 0))
        self.showImage("images/title_initial.png", (0, 40), (int(1996 / 2), int(627 / 2)))
        self.showImage("images/maze.png", (self.size[0]/2 - 50, 150))


        game_loop = True
        while game_loop:

            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():

                if (event.type == pygame.QUIT):
                    game_loop = False

            if (self.size[0]/2 - 180) <= mx <= (self.size[0]/2 + 180) and 450 <= my <= 555.5:
                self.showImage("images/initial_button_pressed.png", (self.size[0] / 2 - 180, 450), (int(720 / 2), int(231 / 2)))
            else:
                self.showImage("images/initial_button.png", (self.size[0] / 2 - 180, 450), (int(720 / 2), int(231 / 2)))

            pygame.display.flip()

        pygame.quit()





