from threading import Thread

class ParallelThreads:

    @staticmethod
    def findMonstersNewPosition(monster_1, monster_2, monster_3, player, window, maze, player_list):
        thread_1 = Thread(target=monster_1.findNewPosition, args=(player, maze))
        thread_2 = Thread(target=monster_2.findNewPosition, args=(player, maze))
        thread_3 = Thread(target=monster_3.findNewPosition, args=(player, maze))
        thread_4 = Thread(target=window.showMazeScreen, args=(player_list, maze, player.lives))

        thread_1.start()
        thread_2.start()
        thread_3.start()
        thread_4.start()

        thread_1.join()
        thread_2.join()
        thread_3.join()
        thread_4.join()
