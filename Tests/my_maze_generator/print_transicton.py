import pygame


def print_transiction(trans, pxl=50):
    pygame.init()

    # Colors:
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    i = 0

    width = trans.num_cells_x * 2 + 1
    height = trans.num_cells_y * 2 + 1
    screen_width = width * pxl
    screen_height = height * pxl

    background = pygame.display.set_mode([screen_width, screen_height])

    sair = False

    while sair == False:
        background.fill(white)

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                sair = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and i < len(trans.mazesMatrices) - 1:
                    i += 1

        for y in range(height):
            for x in range(width):
                if (trans.mazesMatrices[i][y][x] == 1):
                    pygame.draw.rect(background, black, [x * pxl, y * pxl, pxl, pxl])

        pygame.display.update()

    pygame.quit()

