# import all libraries here

# import all files here
from open_window import *
from character import *
from make_maze import *
from monster import *
from parallel_threads import ParallelThreads

game_maze = Maze(15, 10)

game_window = Window('images/initial_background.jpg', game_maze)

action = game_window.initialWindow()

if action == Action.quit_game:
    game_window.quitGame()
elif action == Action.change_screen:
    player = Character(35, 35, 3)
    player_list = pygame.sprite.Group()
    red_monster = Monster('images/monster1.png', 33, 605, 2)
    green_monster = Monster('images/monster2.png', 935, 32, 2)
    ugly_monster = Monster('images/monster3.png', 935, 32, 1)
    player_list.add(player)
    player_list.add(red_monster)
    player_list.add(green_monster)
    player_list.add(ugly_monster)

    red_monster.findNewPosition(player, game_maze)
    red_monster.getNextPosition(game_window)


    action = Action.stand_by

    while action == Action.stand_by:
        game_window.showMazeScreen(player_list, game_maze, player.lives)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                action = Action.quit_game

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[ord('a')]:
            player.control(0, -4, game_maze, game_window)
            red_monster.updatePosition(game_maze, game_window)
            green_monster.updatePosition(game_maze, game_window)
            ugly_monster.updatePosition(game_maze, game_window)
            ParallelThreads.findMonstersNewPosition(red_monster, green_monster, ugly_monster, player, game_window, game_maze, player_list)


        elif keys[pygame.K_RIGHT] or keys[ord('d')]:
            player.control(0, 4, game_maze, game_window)
            red_monster.updatePosition(game_maze, game_window)
            green_monster.updatePosition(game_maze, game_window)
            ugly_monster.updatePosition(game_maze, game_window)
            ParallelThreads.findMonstersNewPosition(red_monster, green_monster, ugly_monster, player, game_window, game_maze, player_list)

        elif keys[pygame.K_UP] or keys[ord('w')]:
            player.control(-4, 0, game_maze, game_window)
            red_monster.updatePosition(game_maze, game_window)
            green_monster.updatePosition(game_maze, game_window)
            ugly_monster.updatePosition(game_maze, game_window)
            ParallelThreads.findMonstersNewPosition(red_monster, green_monster, ugly_monster, player, game_window, game_maze, player_list)

        elif keys[pygame.K_DOWN] or keys[ord('s')]:
            player.control(4, 0, game_maze, game_window)
            red_monster.updatePosition(game_maze, game_window)
            green_monster.updatePosition(game_maze, game_window)
            ugly_monster.updatePosition(game_maze, game_window)
            ParallelThreads.findMonstersNewPosition(red_monster, green_monster, ugly_monster, player, game_window, game_maze, player_list)

        red_monster.updatePosition(game_maze, game_window)
        green_monster.updatePosition(game_maze, game_window)
        ugly_monster.updatePosition(game_maze, game_window)
        action = player.detectMonsterCollision(red_monster, green_monster, ugly_monster, game_maze)


    if action == Action.player_dead:
        game_window.showEndScreen()

    if action == Action.quit_game:
        game_window.quitGame()


