from character import *
from maze import *
from monster import *
from parallel_threads import ParallelThreads
import time


class GameController:

    playing_time = 0

    def __init__(self, maze_shape):
        self.game_window = Window('images/initial_background.jpg', maze_shape)

    def quitGame(self):
        pygame.quit()

    def showInitialWindow(self):
        self.game_window.initialWindow()
        action = Action.stand_by
        while action == Action.stand_by:

            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    action = Action.quit_game
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (self.game_window.size[0] / 2 - 180) <= mx <= (self.game_window.size[0] / 2 + 180) and \
                            450 <= my <= 555.5:
                        action = Action.change_screen

            if (self.game_window.size[0] / 2 - 180) <= mx <= (self.game_window.size[0] / 2 + 180) and\
                    450 <= my <= 555.5:
                self.game_window.window.blit(self.game_window.pressed_start_button, (self.game_window.size[0] / 2 - 180,
                                                                                     450))

            else:
                self.game_window.window.blit(self.game_window.start_button, (self.game_window.size[0] / 2 - 180, 450))

            pygame.display.flip()

        return action

    def playGame(self, maze_shape):
        player = Character(35, 35, 3)
        game_maze = Maze(maze_shape[0], maze_shape[1])
        player_list = pygame.sprite.Group()
        red_monster = Monster('images/monster1.png', 33, 605, 2)
        green_monster = Monster('images/monster2.png', 935, 32, 2)
        ugly_monster = Monster('images/monster3.png', 935, 32, 1)
        player_list.add(player)
        player_list.add(red_monster)
        player_list.add(green_monster)
        player_list.add(ugly_monster)

        red_monster.findNewPosition(player, game_maze)
        red_monster.getNextPosition(self.game_window)

        action_local = Action.stand_by

        start_time = time.time()

        while action_local == Action.stand_by:
            self.game_window.showMazeScreen(player_list, game_maze, player.lives)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[ord('a')]:
                player.control(0, -4, game_maze, self.game_window)
                red_monster.updatePosition(game_maze, self.game_window)
                green_monster.updatePosition(game_maze, self.game_window)
                ugly_monster.updatePosition(game_maze, self.game_window)
                ParallelThreads.findMonstersNewPosition(red_monster, green_monster, ugly_monster, player,
                                                        self.game_window, game_maze, player_list)

            elif keys[pygame.K_RIGHT] or keys[ord('d')]:
                player.control(0, 4, game_maze, self.game_window)
                red_monster.updatePosition(game_maze, self.game_window)
                green_monster.updatePosition(game_maze, self.game_window)
                ugly_monster.updatePosition(game_maze, self.game_window)
                ParallelThreads.findMonstersNewPosition(red_monster, green_monster, ugly_monster, player,
                                                        self.game_window, game_maze, player_list)

            elif keys[pygame.K_UP] or keys[ord('w')]:
                player.control(-4, 0, game_maze, self.game_window)
                red_monster.updatePosition(game_maze, self.game_window)
                green_monster.updatePosition(game_maze, self.game_window)
                ugly_monster.updatePosition(game_maze, self.game_window)
                ParallelThreads.findMonstersNewPosition(red_monster, green_monster, ugly_monster, player,
                                                        self.game_window, game_maze, player_list)

            elif keys[pygame.K_DOWN] or keys[ord('s')]:
                player.control(4, 0, game_maze, self.game_window)
                red_monster.updatePosition(game_maze, self.game_window)
                green_monster.updatePosition(game_maze, self.game_window)
                ugly_monster.updatePosition(game_maze, self.game_window)
                ParallelThreads.findMonstersNewPosition(red_monster, green_monster, ugly_monster, player,
                                                        self.game_window, game_maze, player_list)

            red_monster.updatePosition(game_maze, self.game_window)
            green_monster.updatePosition(game_maze, self.game_window)
            ugly_monster.updatePosition(game_maze, self.game_window)
            action_local = player.detectMonsterCollision(red_monster, green_monster, ugly_monster,game_maze)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    action_local = Action.quit_game

        end_time = time.time()

        self.playing_time = end_time - start_time

        return action_local

    def endScreen(self):
        self.game_window.showEndScreen(self.playing_time)

        action = Action.local_loop

        while action == Action.local_loop:

            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    action = Action.quit_game
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (self.game_window.size[0] / 4 - 180) <= mx <= (self.game_window.size[0] / 4 + 180) and \
                            500 <= my <= 605.5:
                        action = Action.stand_by
                    elif (3*self.game_window.size[0] / 4 - 180) <= mx <= (3*self.game_window.size[0] / 4 + 180) and \
                            500 <= my <= 605.5:
                        action = Action.quit_game

            if (self.game_window.size[0] / 4 - 180) <= mx <= (self.game_window.size[0] / 4 + 180) and \
                    500 <= my <= 605.5:
                self.game_window.window.blit(self.game_window.pressed_restart_button, ((self.game_window.size[0] / 4 - 180), 500))

            else:
                self.game_window.window.blit(self.game_window.restart_button, ((self.game_window.size[0] / 4 - 180), 500))

            if (3*self.game_window.size[0] / 4 - 180) <= mx <= (3*self.game_window.size[0] / 4 + 180) and \
                    500 <= my <= 605.5:
                self.game_window.window.blit(self.game_window.pressed_exit_button, ((3*self.game_window.size[0] / 4 - 180), 500))

            else:
                self.game_window.window.blit(self.game_window.exit_button, ((3*self.game_window.size[0] / 4 - 180), 500))

            pygame.display.flip()

        return action
