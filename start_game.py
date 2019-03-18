# import all libraries here

# import all files here
from open_window import *
from make_maze import *

game_maze = Maze(5, 5)
print(game_maze.maze)

game_maze.newMaze(10, 10)
print(game_maze.maze)



game_window = Window((1000,667), 'images/initial_background.jpg')

action = game_window.initialWindow()

if action == Action.quit_game:
    game_window.quitGame()
elif action == Action.change_screen:
    game_window.showMazeScreen()


