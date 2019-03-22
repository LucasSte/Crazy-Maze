# import all libraries here

# import all files here
from open_window import *
from character import *
from make_maze import *


game_window = Window('images/initial_background.jpg')

action = game_window.initialWindow()

if action == Action.quit_game:
    game_window.quitGame()
elif action == Action.change_screen:
    player = Character(game_window.size[0]/2, game_window.size[1]/2)
    player_list = pygame.sprite.Group()
    player_list.add(player)
    game_maze = Maze(25, 15)
    game_maze = Maze(25, 15)

    action = Action.stand_by

    while action == Action.stand_by:
        game_window.showMazeScreen(player_list, game_maze)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                action = Action.quit_game

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[ord('a')]:
            player.control(0, -1)
        if keys[pygame.K_RIGHT] or keys[ord('d')]:
            player.control(0, 1)
        if keys[pygame.K_UP] or keys[ord('w')]:
            player.control(-1, 0)
        if keys[pygame.K_DOWN] or keys[ord('s')]:
            player.control(1, 0)

    if action == Action.quit_game:
        game_window.quitGame()


