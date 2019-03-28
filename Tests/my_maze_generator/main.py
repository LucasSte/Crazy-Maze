# import all libraries here
import numpy as np
import copy

# import all files here
from make_maze import *
from print_transicton import *
from print_maze import *
from transition import *


game_maze = Maze(20, 20, [3, 3])


oldMaze = copy.copy(game_maze)
game_maze = Maze(20, 20, [5, 5])

trans = Transiction(oldMaze, game_maze, [10, 10])

print_transiction(trans, 15)





