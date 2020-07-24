import pygame
import time
import random

pygame.init()

game_width = 800
game_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 0, 255)
start_x = 0
start_y = 1

gameWindow = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption('snake Game')
pygame.display.update()

block = 20
FPS = 13

clk = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)


def snake(block, snakelist):
    for xny in snakelist:
        pygame.draw.rect(gameWindow, blue, [xny[0], xny[1], block, block])


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameWindow.blit(screen_text, [game_width / 4, game_height / 2])


def loop():
    gameOver = False
    gameClose = False
    rApplex = round(random.randrange(0, game_width - block) / 20.0) * 20.0
    rAppley = round(random.randrange(0, game_height - block) / 20.0) * 20.0

    start_x = game_width / 2
    start_y = game_height / 2
    update_x = 0
    update_y = 0
    snakeList = []
    snakeLength = 1
    while not gameClose:
        while gameOver == True:
            gameWindow.fill(white)
            message_to_screen("You looose!!!!, Press 'r' to replay or press 'q' to Quit ", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameClose = True
                        gameOver = False
                    if event.key == pygame.K_r:
                        loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameClose = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    update_x = -block
                    update_y = 0

                if event.key == pygame.K_RIGHT:
                    update_x = +block
                    update_y = 0

                if event.key == pygame.K_UP:
                    update_y = -block
                    update_x = 0

                if event.key == pygame.K_DOWN:
                    update_y = +block
                    update_x = 0

        if start_x >= game_width or start_x < 0 or start_y >= game_height or start_y < 0:
            gameOver = True

        start_x += update_x
        start_y += update_y
        gameWindow.fill(yellow)
        pygame.draw.rect(gameWindow, red, [rApplex, rAppley, block, block])
        # pygame.draw.line(gameWindow,white,[0,0],[50,30],6 )
        # pygame.draw.rect(gameWindow, blue, [start_x, start_y, block, block])
        # pygame.draw.polygon(gameWindow, black, [[100, 100], [0, 200], [200, 200]], 5)
        # pygame.draw.circle(gameWindow, blue, [400, 300], 70, 6)

        snakeHead = []
        snakeHead.append(start_x)
        snakeHead.append(start_y)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del (snakeList[0])

        for easement in snakeList[:-1]:
            if easement == snakeHead:
                gameOver = True

                snake(block, snakeList)
        pygame.display.update()

        if start_x == rApplex and start_y == rAppley:
            rApplex = round(random.randrange(0, game_width - block) / 20.0) * 20.0
            rAppley = round(random.randrange(0, game_height - block) / 20.0) * 20.0
            snakeLength += 1

        clk.tick(FPS)

    pygame.quit()
    quit()


loop()
