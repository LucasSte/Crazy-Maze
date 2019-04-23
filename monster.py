import pygame
from open_window import Window
from algorithm import Algorithm
from algorithm import AuxFunc
from enum import Enum


class Move(Enum):
    up = 1
    left = 2
    down = 3
    right = 4


class Monster(pygame.sprite.Sprite):

    path_to_player = list()
    last_monster_node_x = -1
    last_monster_node_y = -1
    aStar_delay = 20
    aStar_counter = 0
    last_movement = 0

    def __init__(self, image_path, node, speed, window):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.size = (20, 20)
        self.frame = 0
        image_aux = pygame.image.load(image_path)
        image_aux = pygame.transform.scale(image_aux, self.size)
        self.image = image_aux
        self.rect = self.image.get_rect()
        start_position_x = node[0]*window.pxl_x + 1
        start_position_y = node[1]*window.pxl_y + 1
        self.start_position = (start_position_x, start_position_y)
        self.rect.x = start_position_x
        self.rect.y = start_position_y
        self.speed = speed

    def resetPosition(self):
        self.rect.x = self.start_position[0]
        self.rect.y = self.start_position[1]

    def getMonsterNode(self, maze): # of your center

        matrix_shape = maze.matrix.shape

        monster_matrix_x = int((self.rect.x+self.size[0]/2)*matrix_shape[1]/Window.size[0])
        monster_matrix_y = int((self.rect.y+self.size[1]/2)*matrix_shape[0]/Window.size[1])

        monster_node = (monster_matrix_y, monster_matrix_x)

        return monster_node

    def findNewPath(self, player, game_controller):

        # aStar eh muito pesado e estava causando lag no jogo, adicionei um delay para sua execucao:
        if self.aStar_counter == 0 or self.aStar_counter > self.aStar_delay:
            player_node = player.getCharacterNode(game_controller)
            monster_node = self.getMonsterNode(game_controller)
            if game_controller.matrix[player_node[0]][player_node[1]] == 0:
                if self.last_monster_node_x != monster_node[0] or self.last_monster_node_y != monster_node[1]:
                    self.path_to_player = Algorithm.aStar(game_controller.matrix, monster_node, player_node)

            self.aStar_counter = 0

        self.aStar_counter = self.aStar_counter + 1


    def inOnlyOneNode(self, maze):
        up_left_corner = AuxFunc.getNode(self.rect.x, self.rect.y, maze)
        up_right_corner = AuxFunc.getNode(self.rect.x+self.size[0], self.rect.y, maze)

        if up_left_corner[0] != up_right_corner[0] or up_left_corner[1] != up_right_corner[1]:
            return False
        down_left_corner = AuxFunc.getNode(self.rect.x, self.rect.y + self.size[1], maze)
        if up_left_corner[0] != down_left_corner[0] or up_left_corner[1] != down_left_corner[1]:
            return False
        down_right_corner = AuxFunc.getNode(self.rect.x + self.size[0], self.rect.y+self.size[1], maze)
        if up_left_corner[0] != down_right_corner[0] or up_left_corner[1] != down_right_corner[1]:
            return False
        else:
            return True

    def updatePosition(self, maze):
        if self.path_to_player is not None and len(self.path_to_player) > 0:
            next_node = self.path_to_player[-1]
            # monster's current position:
            up_left_corner_pos = self.rect.x, self.rect.y, maze
            up_left_corner_node = AuxFunc.getNode(up_left_corner_pos[0], up_left_corner_pos[1], maze)
            down_right_corner_pos = self.rect.x + self.size[0], self.rect.y + self.size[1], maze
            down_right_corner_node = AuxFunc.getNode(down_right_corner_pos[0], down_right_corner_pos[1], maze)

            next_pos = (next_node[1]*maze.pxl_x, next_node[0]*maze.pxl_y)
            image = pygame.image.load("images/heart.png")
            image = pygame.transform.scale(image, (24, 24))
            maze.window.blit(image, next_pos)

            desired_node1 = AuxFunc.getNode(up_left_corner_pos[0], up_left_corner_pos[1]-self.speed, maze)
            desired_node2 = AuxFunc.getNode(down_right_corner_pos[0], up_left_corner_pos[1]+self.speed, maze)
            desired_node3 = AuxFunc.getNode(down_right_corner_pos[0]-self.speed, down_right_corner_pos[1], maze)
            desired_node4 = AuxFunc.getNode(up_left_corner_pos[0]+self.speed, down_right_corner_pos[1], maze)


            if down_right_corner_node[0] - next_node[0] > 0 and \
                    maze.matrix[desired_node1[0], desired_node1[1]] == 0 and \
                    maze.matrix[desired_node2[0], desired_node2[1]] == 0:
                self.rect.y -= self.speed
                self.last_movement = Move.up
            elif up_left_corner_node[0] - next_node[0] < 0 and \
                    maze.matrix[desired_node3[0], desired_node3[1]] == 0 and \
                    maze.matrix[desired_node4[0], desired_node4[1]] == 0:
                self.rect.y += self.speed
                self.last_movement = Move.down
            elif down_right_corner_node[1] - next_node[1] > 0 and \
                    maze.matrix[desired_node1[0], desired_node1[1]] == 0 and \
                    maze.matrix[desired_node4[0], desired_node4[1]] == 0:
                    self.rect.x -= self.speed
                    self.last_movement = Move.left
            elif up_left_corner_node[1] - next_node[1] < 0 and \
                    maze.matrix[desired_node2[0], desired_node2[1]] == 0 and \
                    maze.matrix[desired_node3[0], desired_node3[1]] == 0:
                self.rect.x += self.speed
                self.last_movement = Move.right

            # se nao conseguiu mover-se para onde quer, repete o ultimo movimento:
            if self.last_movement == Move.right:
                self.rect.x += self.speed
            elif self.last_movement == Move.down:
                self.rect.y += self.speed
            elif self.last_movement == Move.left:
                self.rect.x -= self.speed
            elif self.last_movement == Move.up:
                self.rect.y -= self.speed

            # se nao conseguiu mover-se para onde quer, vai para onde pode:
            # elif maze.matrix[desired_node2[0], desired_node2[1]] == 0 and \
            #         maze.matrix[desired_node3[0], desired_node3[1]] == 0:
            #     self.rect.x += self.speed
            #     self.last_movement = Move.right
            # elif maze.matrix[desired_node3[0], desired_node3[1]] == 0 and \
            #         maze.matrix[desired_node4[0], desired_node4[1]] == 0:
            #     self.rect.y += self.speed
            #     self.last_movement = Move.down
            # elif maze.matrix[desired_node1[0], desired_node1[1]] == 0 and \
            #         maze.matrix[desired_node4[0], desired_node4[1]] == 0:
            #         self.rect.x -= self.speed
            #         self.last_movement = Move.left
            # elif maze.matrix[desired_node1[0], desired_node1[1]] == 0 and \
            #         maze.matrix[desired_node2[0], desired_node2[1]] == 0:
            #     self.rect.y -= self.speed
            #     self.last_movement = Move.up


            if self.getMonsterNode(maze) == next_node:
                self.path_to_player.pop()
