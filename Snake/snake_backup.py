import pygame
import random
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

gameDisplay= pygame.display.set_mode ((display_width,display_height))
pygame.display.set_caption('Snakesss')
clock = pygame.time.Clock()

def cria_cobra(x,y):
        pygame.draw.rect(gameDisplay, black,[x,y,10,10])

def cria_comida(x,y):
        pygame.draw.circle(gameDisplay,black,[x,y],5)

def game_loop():
    

    x = (display_width/2)
    y = (display_height/2)

    x_change = 0
    y_change = 0
    gameExit = False

    while not gameExit:
        
        for event in pygame.event.get():
                
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        y_change = -5
                        x_change = 0
                    elif event.key == pygame.K_DOWN:
                        y_change = 5
                        x_change = 0
                    if event.key == pygame.K_LEFT:
                        x_change = -5
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = 5
                        y_change = 0

                
                    
        #print(event)

        x += x_change
        y += y_change
        print('x:',x)
        print('x_cahnge',x_change)

        gameDisplay.fill(white)
        cria_cobra(x,y)
        cria_comida(random.randrange(0,display_width),random.randrange(0,display_height))
        
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
