import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)

smallText = pygame.font.Font("freesansbold.ttf", 20)
mediumText = pygame.font.Font("freesansbold.ttf", 70)
largeText = pygame.font.Font('freesansbold.ttf', 115)

def score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))

FPS = 30
block_size = 10


clock = pygame.time.Clock()

def snake(block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])

def message_to_screen(msg,color):
    screen_text = smallText.render(msg,True,color) #a mensagem
    gameDisplay.blit(screen_text, [display_width/2,display_height/2]) #colocar no ecra

def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    snakelist = []
    snakeLength = 1
    randAppleX = round(random.randrange(0,display_width-block_size)/10.0)*10.0
    randAppleY = round(random.randrange(0,display_height-block_size)/10.0)*10.0

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press c to continue or q to quit",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver= False

                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_x_change = 0
                    lead_y_change = -block_size
                elif event.key == pygame.K_DOWN:
                    lead_x_change = 0
                    lead_y_change = block_size
        if (lead_x + block_size) >= display_width or lead_x < 1 or (lead_y+block_size) >= display_height or lead_y < 0:
            gameOver = True


        lead_x += lead_x_change
        lead_y += lead_y_change


        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [randAppleX,randAppleY, block_size,block_size])


        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakelist.append(snakeHead)

        if len(snakelist) > snakeLength:
            del snakelist[0]

        for eachSegment in snakelist[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakelist)
        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
                randAppleX = round(random.randrange(0,display_width-block_size)/10.0)*10.0
                randAppleY = round(random.randrange(0,display_height-block_size)/10.0)*10.0
                snakeLength += 1


        clock.tick(FPS)

    pygame.quit()
    quit()


gameLoop()
