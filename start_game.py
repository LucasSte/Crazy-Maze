# import all libraries here

# import all files here
from open_window import *
from character import *
from make_maze import *
from monster import *

game_maze = Maze(15, 10)

game_window = Window('images/initial_background.jpg', game_maze)

action = game_window.initialWindow()

if action == Action.quit_game:
    game_window.quitGame()
elif action == Action.change_screen:
    player = Character(35, 35)
    player_list = pygame.sprite.Group()
    red_monster = Monster('images/monster1.png', 33, 605)
    player_list.add(player)
    player_list.add(red_monster)

    red_monster.findNewPosition(player, game_maze)
    red_monster.getNextPosition(game_window)


    action = Action.stand_by

    while action == Action.stand_by:
        game_window.showMazeScreen(player_list, game_maze)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                action = Action.quit_game

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    red_monster.getNextPosition(game_window)
                    red_monster.updatePosition(game_window)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[ord('a')]:
            player.control(0, -2, game_maze, game_window)
            red_monster.findNewPosition(player, game_maze)
            #red_monster.getNextPosition(game_window)
        elif keys[pygame.K_RIGHT] or keys[ord('d')]:
            player.control(0, 2, game_maze, game_window)
            red_monster.findNewPosition(player, game_maze)
            #red_monster.getNextPosition(game_window)
        elif keys[pygame.K_UP] or keys[ord('w')]:
            player.control(-2, 0, game_maze, game_window)
            red_monster.findNewPosition(player, game_maze)
            #red_monster.getNextPosition(game_window)
        elif keys[pygame.K_DOWN] or keys[ord('s')]:
            player.control(2, 0, game_maze, game_window)
            red_monster.findNewPosition(player, game_maze)
            #red_monster.getNextPosition(game_window)



    if action == Action.quit_game:
        game_window.quitGame()


