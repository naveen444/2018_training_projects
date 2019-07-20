import pygame
import random

pygame.init()

red = 255,0,0
black = 0,0,0
white = 255,255,255

width = 900
height = 600

screen = pygame.display.set_mode((width,height))

frog = pygame.image.load("frog.png")
snake_bg = pygame.image.load('snakebg.jpg')

clock = pygame.time.Clock()

def homeScreen():
    message = "Press SPACE to start the game"
    font = pygame.font.Font('zorque.ttf', 50)
    text = font.render(message, True, black)
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        screen.blit(snake_bg, (0,0))
        screen.blit(text, (width / 2 - 400, height / 2 - 100))

        pygame.display.update()


def gameOver():
    message = "Game Over"
    font = pygame.font.Font('zorque.ttf',50)
    text = font.render(message, True, black)
    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(text, (width/2 - 100,height/2 - 100))

        pygame.display.update()

def score(counter):
    # font = pygame.font.SysFont(None,45)
    font = pygame.font.Font('zorque.ttf',45)
    text = font.render("Score : "+str(counter), True, red)
    screen.blit(text, (width - 300,10))

def snake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen,red,[snakeList[i][0], snakeList[i][1], 50, 50])

def game():
    frog_width = frog.get_width()
    frog_height = frog.get_height()
    frog_x = random.randint(0, width - frog_width)
    frog_y = random.randint(0, height - frog_height)
    x = 0
    y = 0
    move_x = 0
    move_y = 0
    snakeList = []
    snakeLength = 1

    counter = 0

    coin_sound = pygame.mixer.Sound('point.wav')

    FPS = 90

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_x = 5
                    move_y = 0
                elif event.key == pygame.K_LEFT:
                    move_x = -5
                    move_y = 0
                elif event.key == pygame.K_DOWN:
                    move_y = 5
                    move_x = 0
                elif event.key == pygame.K_UP:
                    move_y = -5
                    move_x = 0

        screen.fill(white)

        # snake_rect = pygame.draw.rect(screen,red,[x,y,50,50])
        snake_rect = pygame.Rect(x, y, 50, 50)

        screen.blit(frog, (frog_x, frog_y))
        frog_rect = pygame.Rect(frog_x,frog_y,frog_width,frog_height)

        x += move_x
        y += move_y

        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)
        snakeList.append(snakeHead)
        # print(snakeList)
        if len(snakeList) > snakeLength:
            del snakeList[0]

        snake(snakeList)
        score(counter)

        if snake_rect.colliderect(frog_rect):
            frog_x = random.randint(0, width - frog_width)
            frog_y = random.randint(0, height - frog_height)
            snakeLength += 10
            FPS += 1
            counter += 1
            coin_sound.play()

        for each in snakeList[:-1]:
            if each == snakeList[-1]:
                # print("Game Over")
                gameOver()

        if x > width:
            x = -50
        elif y > height:
            y = -50
        elif x < -50:
            x = width
        elif y < -50:
            y = height

        pygame.display.update()
        clock.tick(FPS)

# game()
homeScreen()