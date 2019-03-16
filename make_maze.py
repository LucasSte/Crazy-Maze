import pygame
from random import shuffle, randrange

# Não sei o que faz, entao mantive
MISSING = object()


class Maze:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        pygame.init()
        self.maze = self.makeMaze()

    def newMaze(self, newWidth, newHeight):
        self.__init__(newWidth, newHeight)

    def makeMaze(self):

        # casas a serem visitadas:
        vis = [[0] * self.width + [1] for _ in range(self.height)] + [[1] * (self.width + 1)]

        # Paredes verticais:
        ver = [["10"] * self.width + ['1'] for _ in range(self.height)] + [[]]

        # Paredes horizontais:
        hor = [["11"] * self.width + ['1'] for _ in range(self.height + 1)]

        def walk(x, y):
            vis[y][x] = 1

            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(d)
            for (xx, yy) in d:
                if vis[yy][xx]: continue
                if xx == x: hor[max(y, yy)][x] = "10"
                if yy == y: ver[y][max(x, xx)] = "00"
                walk(xx, yy)

        walk(randrange(self.width), randrange(self.height))

        s = ""
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])

        return s