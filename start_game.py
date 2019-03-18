#import all libraries here

#import all files here
from open_window import *
from character import *


game_window = Window('images/initial_background.jpg')

action = game_window.initialWindow()

if action == Action.quit_game:
    game_window.quitGame()
elif action == Action.change_screen:
    #game_window.showImage('images/maze.png', (game_window.size[0] / 2, game_window.size[1] / 2))
    player = Character(game_window.size[0]/2, game_window.size[1]/2)
    player_list = pygame.sprite.Group()
    player_list.add(player)


    action = -1

    while action == -1:
        game_window.showMazeScreen(player_list)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                action = Action.quit_game

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[ord('a')]:
            player.control(0, -0.5)
        if keys[pygame.K_RIGHT] or keys[ord('d')]:
            player.control(0, 0.5)
        if keys[pygame.K_UP] or keys[ord('w')]:
            player.control(-0.5, 0)
        if keys[pygame.K_DOWN] or keys[ord('s')]:
            player.control(0.5, 0)

    if action == Action.quit_game:
        game_window.quitGame()


