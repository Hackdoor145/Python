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

def player(player_x,player_y,color):
    pygame.draw.rect(gameDisplay, color, [player_x, player_y, 10, 100])

def ai(ai_x,ai_y,color):
    pygame.draw.rect(gameDisplay, color, [ai_x, ai_y, 10, 100])

def ball(ball_x,ball_y,color):
    pygame.draw.circle(gameDisplay, color, (ball_x,ball_y),15)

def game_loop():
    player_x = 100
    player_y = (display_height/2)-50

    y_change = 0

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

            player_y += y_change


            gameDisplay.fill(black)
            player(player_x,player_y,white)
            ai(ai_x,ai_y,white)
            ball(400,300,white)

            pygame.display.update()
            clock.tick(30)

game_loop()
pygame.quit()
quit()
