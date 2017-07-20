import pygame


pygame.init()

display_width = 800
display_height = 600

smallText = pygame.font.Font("freesansbold.ttf", 20)
mediumText = pygame.font.Font("freesansbold.ttf", 70)
largeText = pygame.font.Font('freesansbold.ttf', 115)

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pong!')
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def player(player_x,player_y,color):
    pygame.draw.rect(gameDisplay, color, [player_x, player_y, 10, 100])

def ai(ai_x,ai_y,color):
    pygame.draw.rect(gameDisplay, color, [ai_x, ai_y, 10, 100])

def ball(ball_x,ball_y,color):
    pygame.draw.circle(gameDisplay, color, (ball_x,ball_y),15)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_green, (150, 450, 100, 50))
            game_loop()
        else:
            pygame.draw.rect(gameDisplay, green, (150, 450, 100, 50))

        textSurf, textRect = text_objects("GO!", smallText)
        textRect.center = ((150 + (100 / 2)), (450 + (50 / 2)))
        gameDisplay.blit(textSurf, textRect)

        if 550 + 100 > mouse[0] > 550 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_red, (550, 450, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))

        textSurf, textRect = text_objects("Quit", smallText)
        textRect.center = ((550 + (100 / 2)), (450 + (50 / 2)))
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    player_x = 100
    player_y = (display_height/2)-50

    y_change = 0

    ball_x = 400
    ball_y = 300
    ball_speed = 10

    ai_x = 700
    ai_y = player_y

    gameExit = False

    while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        y_change = -5
                    elif event.key == pygame.K_DOWN:
                        y_change = 5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        y_change = 0

            if ball_x >= display_height:
                ball_speed -= 1
            elif ball_x <= 0:
                ball_speed.__invert__
            elif ball_y >= display_width:
                ball_speed -= 1
            elif ball_y <= 0:
                ball_speed += 1

            ball_x += 1 + ball_speed
            ball_y += 1 + ball_speed

            player_y += y_change


            gameDisplay.fill(black)
            player(player_x,player_y,white)
            ai(ai_x,ai_y,white)
            ball(ball_x,ball_y,white)



            pygame.display.update()
            clock.tick(30)

#game_intro()
game_loop()
pygame.quit()
quit()
