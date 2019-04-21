# import everything here
from game_controller import *
from open_window import Action

game = GameController()

action = Action.stand_by


while action == Action.stand_by:

    action = game.showInitialWindow()

    if action == Action.change_screen:
        action = game.playGame()

    if action == Action.player_dead:
        action = game.endScreen()

    if action == Action.player_win:
        action = game.winningScreen()

    if action == Action.quit_game:
        game.quitGame()



