import pygame
from enum import Enum


class Action(Enum):
    stand_by = -1
    quit_game = 0
    change_screen = 1


MISSING = object()


class Window:

    font_location = "fonts/conthrax-sb.ttf"
    # size = (994, 656)
    size = (1000, 667)
    window = pygame.display.set_mode(size)
    pressed_start_button = pygame.image.load("images/initial_button_pressed.png")
    pressed_start_button = pygame.transform.scale(pressed_start_button, (int(720 / 2), int(231 / 2)))
    start_button = pygame.image.load("images/initial_button.png")
    start_button = pygame.transform.scale(start_button, (int(720 / 2), int(231 / 2)))

    def __init__(self, background, maze):
        self.background = background
        pygame.init()

        # showMazeScreen variables:
        ## Coloquei elas aqui, pois as imagens precisam ser carregadas apenas uma vez, caso contrario, o jogo fica
        ## muito lento
        self.pxl_x = self.size[0] / maze.width
        self.pxl_y = self.size[1] / maze.height

        self.grass_image = pygame.image.load("images/grass2.jpg")
        self.grass_image = pygame.transform.scale(self.grass_image, self.size)

        self.wall_image = pygame.image.load("images/wall.png")
        self.wall_image = pygame.transform.scale(self.wall_image, (int(self.pxl_x + 1), int(self.pxl_y + 1)))

    def showText(self, text, position, font_size, color):
        title_font = pygame.font.Font(self.font_location, font_size)
        text_surface = title_font.render(text, True, color)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = position
        self.window.blit(text_surface, text_rectangle)

    def showImage(self, image_path, position, scale=MISSING):
        image = pygame.image.load(image_path)
        if scale is not MISSING:
            image = pygame.transform.scale(image, scale)
        self.window.blit(image, position)

    def initialWindow(self):
        pygame.display.set_caption("Crazy Maze")
        background_image = pygame.image.load(self.background)
        background_image = pygame.transform.scale(background_image, self.size)
        self.window.blit(self.start_button, (self.size[0] / 2 - 180, 450))
        self.window.blit(background_image, (0, 0))
        self.showImage("images/title_initial.png", (2, 40), (int(1996 / 2), int(667 / 2)))
        action = Action.stand_by
        while action == Action.stand_by:

            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    action = Action.quit_game
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (self.size[0] / 2 - 180) <= mx <= (self.size[0] / 2 + 180) and 450 <= my <= 555.5:
                        action = Action.change_screen

            if (self.size[0] / 2 - 180) <= mx <= (self.size[0] / 2 + 180) and 450 <= my <= 555.5:
                self.window.blit(self.pressed_start_button, (self.size[0] / 2 - 180, 450))

            else:
                self.window.blit(self.start_button, (self.size[0] / 2 - 180, 450))

            pygame.display.flip()

        return action

    def quitGame(self):
        pygame.quit()



    def showMazeScreen(self, player_list, maze):
        color = (255,255,255)
        # self.window.fill(color)
        self.window.blit(self.grass_image, (0, 0))

        # Draw the maze
        for y in range(maze.height):
            for x in range(maze.width):
                if( maze.matrix[y][x] == 1):
                    self.window.blit(self.wall_image, (x*self.pxl_x, y*self.pxl_y))

        player_list.draw(self.window)
        pygame.display.flip()




