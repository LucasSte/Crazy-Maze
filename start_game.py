#import all libraries here

#import all files here
from open_window import *

game_window = Window((1000,667), 'images/initial_background.jpg')

game_window.initialWindow()

game_loop = True

while game_loop:

    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():

        if (event.type == pygame.QUIT):
            game_loop = False

    if (game_window.size[0] / 2 - 180) <= mx <= (game_window.size[0] / 2 + 180) and 450 <= my <= 555.5:
        game_window.window.blit(game_window.pressed_start_button, (game_window.size[0] / 2 - 180, 450))
    else:
        game_window.window.blit(game_window.start_button, (game_window.size[0] / 2 - 180, 450))

    pygame.display.flip()

pygame.quit()
