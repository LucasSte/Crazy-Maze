#import all libraries here

#import all files here
from open_window import *


game_window = Window((1000,667), 'images/initial_background.jpg')

action = game_window.initialWindow()

if action == Action.quit_game:
    game_window.quitGame()
elif action == Action.change_screen:
    game_window.showMazeScreen()


