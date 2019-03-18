import pygame
from enum import Enum


class Action(Enum):
    quit_game = 0
    change_screen = 1


MISSING = object()


class Window:

    font_location = "fonts/conthrax-sb.ttf"
    pressed_start_button = pygame.image.load("images/initial_button_pressed.png")
    pressed_start_button = pygame.transform.scale(pressed_start_button, (int(720 / 2), int(231 / 2)))
    start_button = pygame.image.load("images/initial_button.png")
    start_button = pygame.transform.scale(start_button, (int(720 / 2), int(231 / 2)))

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

    def initialWindow(self):
        pygame.display.set_caption("Crazy Maze")
        background_image = pygame.image.load(self.background)
        background_image = pygame.transform.scale(background_image, self.size)
        self.window.blit(self.start_button, (self.size[0] / 2 - 180, 450))
        self.window.blit(background_image, (0, 0))
        self.showImage("images/title_initial.png", (2, 40), (int(1996 / 2), int(667 / 2)))
        action = -1
        while action == -1:

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

    def showMazeScreen(self):
        color = (255,0,0)
        self.window.fill(color)
        action = -1

        while action == -1:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    action = Action.quit_game

                pygame.display.flip()

        if action == Action.quit_game:
            self.quitGame()





