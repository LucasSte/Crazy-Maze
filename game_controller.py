from character import *
from maze import *
from monster import *
from parallel_threads import ParallelThreads
import time


class GameController(Window):

    playing_time = 0

    def __init__(self, maze_shape):
        Window.__init__(self, 'images/initial_background.jpg', maze_shape)


    def quitGame(self):
        pygame.quit()

    def showInitialWindow(self):
        self.initialWindow()
        action = Action.stand_by
        while action == Action.stand_by:

            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    action = Action.quit_game
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (self.size[0] / 2 - 180) <= mx <= (self.size[0] / 2 + 180) and \
                            450 <= my <= 555.5:
                        action = Action.change_screen

            if (self.size[0] / 2 - 180) <= mx <= (self.size[0] / 2 + 180) and\
                    450 <= my <= 555.5:
                self.window.blit(self.pressed_start_button, (self.size[0] / 2 - 180,
                                                                                     450))

            else:
                self.window.blit(self.start_button, (self.size[0] / 2 - 180, 450))

            pygame.display.flip()

        return action

    def playGame(self, maze_shape):
        game_maze = Maze(maze_shape[0], maze_shape[1])

        player = Character(3, self)
        player_list = pygame.sprite.Group()

        red_monster = Monster('images/monster1.png', (1, game_maze.height - 2), 2, self)
        green_monster = Monster('images/monster2.png', (game_maze.width - 2, 1), 1, self)
        ugly_monster = Monster('images/monster3.png', (game_maze.width - 2, 1), 2, self)
        player_list.add(player)
        player_list.add(red_monster)
        player_list.add(green_monster)
        player_list.add(ugly_monster)

        # red_monster.findNewPath(player, game_maze)
        # red_monster.getNextPosition(self.game_window)

        action_local = Action.stand_by

        start_time = time.time()

        while action_local == Action.stand_by:

            # update maze:
            game_maze.updateMaze(player.getCharacterNode(game_maze, self))
            self.showMazeScreen(player_list, game_maze, player.lives)
            ParallelThreads.findMonstersNewPosition(red_monster, green_monster, ugly_monster, player,
                                                    self, game_maze, player_list)

            # Move characters
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[ord('a')]:
                player.control(0, -1, game_maze)
                red_monster.updatePosition(game_maze)
                green_monster.updatePosition(game_maze)
                ugly_monster.updatePosition(game_maze)
                ParallelThreads.findMonstersNewPosition(red_monster, green_monster, ugly_monster, player,
                                                        self, game_maze, player_list)

            elif keys[pygame.K_RIGHT] or keys[ord('d')]:
                player.control(0, 1, game_maze)
                red_monster.updatePosition(game_maze)
                green_monster.updatePosition(game_maze)
                ugly_monster.updatePosition(game_maze)
                ParallelThreads.findMonstersNewPosition(red_monster, green_monster, ugly_monster, player,
                                                        self, game_maze, player_list)

            elif keys[pygame.K_UP] or keys[ord('w')]:
                player.control(-1, 0, game_maze)
                red_monster.updatePosition(game_maze)
                green_monster.updatePosition(game_maze)
                ugly_monster.updatePosition(game_maze)
                ParallelThreads.findMonstersNewPosition(red_monster, green_monster, ugly_monster, player,
                                                        self, game_maze, player_list)

            elif keys[pygame.K_DOWN] or keys[ord('s')]:
                player.control(1, 0, game_maze)
                red_monster.updatePosition(game_maze)
                green_monster.updatePosition(game_maze)
                ugly_monster.updatePosition(game_maze)
                ParallelThreads.findMonstersNewPosition(red_monster, green_monster, ugly_monster, player,
                                                        self, game_maze, player_list)

            red_monster.updatePosition(game_maze)
            green_monster.updatePosition(game_maze)
            ugly_monster.updatePosition(game_maze)

            action_local = player.detectMonsterCollision(red_monster, green_monster, ugly_monster,
                                                         game_maze, self)
            action_local = player.detectWin(game_maze, action_local, self)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    action_local = Action.quit_game

        self.playing_time = time.time() - start_time

        return action_local

    def endScreen(self):
        exit_position = ((3 * self.size[0] / 4 - 180), 500)
        restart_position = (self.size[0] / 4 - 180, 500)

        self.showEndScreen(self.playing_time)

        action = Action.local_loop

        while action == Action.local_loop:

            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    action = Action.quit_game
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_position[0] <= mx <= restart_position[0]+360 and \
                            500 <= my <= 605.5:
                        action = Action.stand_by
                    elif exit_position[0] <= mx <= exit_position[0] + 360 and \
                            500 <= my <= 605.5:
                        action = Action.quit_game

            if restart_position[0] <= mx <= restart_position[0]+360 and \
                    500 <= my <= 605.5:
                self.window.blit(self.pressed_restart_button, (restart_position[0], 500))

            else:
                self.window.blit(self.restart_button, (restart_position[0], 500))

            if exit_position[0] <= mx <= exit_position[0] + 360 and \
                    500 <= my <= 605.5:
                self.window.blit(self.pressed_exit_button, (exit_position[0], 500))

            else:
                self.window.blit(self.exit_button, (exit_position[0], 500))

            pygame.display.flip()

        return action

    def winningScreen(self):
        restart_position = (self.size[0] / 4 - 235, 490)
        exit_position = ((3 * self.size[0] / 4 - 140), 490)

        self.showWinningScreen(self.playing_time)

        action = Action.local_loop

        while action == Action.local_loop:

            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    action = Action.quit_game
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_position[0] <= mx <= restart_position[0]+360 and \
                            restart_position[1] <= my <= restart_position[1] + 105.5:
                        action = Action.stand_by
                    elif (3 * self.size[0] / 4 - 180) <= mx <= (3 * self.size[0] / 4 + 180) and \
                            exit_position[1] <= my <= exit_position[1] + 105.5:
                        action = Action.quit_game

            if restart_position[0] <= mx <= restart_position[0]+360 and \
                    restart_position[1] <= my <= restart_position[1] + 105.5:
                self.window.blit(self.pressed_restart_button, (restart_position[0], restart_position[1]))

            else:
                self.window.blit(self.restart_button, (restart_position[0], restart_position[1]))

            if (3 * self.size[0] / 4 - 180) <= mx <= (3 * self.size[0] / 4 + 180) and \
                    exit_position[1] <= my <= exit_position[1] + 105.5:
                self.window.blit(self.pressed_exit_button, exit_position)

            else:
                self.window.blit(self.exit_button, exit_position)

            pygame.display.flip()

        return action
