import pygame
import random
from pygame.locals import*

pygame.init()

width = 1200
height = 500

black = 0,0,0
white = 255,255,255
red = 255,0,0
blue = 0,0,255

screen = pygame.display.set_mode((width, height))

enemyShootSound = pygame.mixer.Sound("sounds/sound_1.wav")
myShipShootSound = pygame.mixer.Sound("sounds/sound_2.wav")
bgImage = pygame.image.load("images/background.jpg")

fontPath = "Atarian/SF Atarian System Bold.ttf"

def homeScreen():
    font = pygame.font.Font(fontPath,100)
    text = font.render("Welcome to Space Shooter", True, white)

    font_2 = pygame.font.Font(fontPath,60)
    text_2 = font_2.render("Press SPACE to start Game",True,white)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # quit pygame
                quit()  # quit python

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        screen.blit(bgImage, (0,0))
        screen.blit(text, (100,100))
        screen.blit(text_2, (250,250))

        pygame.display.update()

def showTimer(seconds):
    font = pygame.font.Font(fontPath, 30)
    text = font.render("Time Left: "+str(seconds), True, black)
    font1 = pygame.font.Font(fontPath, 200)
    text1 = font1.render("game over ", True, black)
    if seconds>0:
        screen.blit(text, (1050,300))
    elif seconds==0:
        screen.blit(text1, (330,100))



def game():

    myShip = pygame.image.load("images/ship_1.png")
    enemyShip = pygame.image.load("images/enemy_2.png")

    myShipWidth = myShip.get_width()
    myShipHeight = myShip.get_height()
    myShipX = width/2 - myShipWidth/2
    myShipY = height - myShipHeight

    enemyWidth = enemyShip.get_width()
    enemyHeight = enemyShip.get_height()

    columns = int(width/enemyShip.get_width())
    # print(int(columns))
    enemyList = []
    # for i in range(columns*2):
    #     enemyList.append(enemyShip)

    for i in range(2):
        for j in range(columns):
            enemyList.append(pygame.Rect(enemyWidth * j, enemyHeight * i, enemyWidth, enemyHeight))

    moveX = 0

    enemyBullet = pygame.Surface((5,15))
    enemyBullet.fill(blue)
    enemyBulletRect = enemyBullet.get_rect()
    randomEnemy = random.choice(enemyList)
    # print(randomEnemy)
    enemyBulletRect.x = randomEnemy.x + enemyWidth/2
    enemyBulletRect.y = randomEnemy.bottom - 20
    enemyShootSound.play()

    bullet = pygame.Surface((5,15))
    bullet.fill(red)
    bulletRect = bullet.get_rect()

    bulletRect.y = myShipY + 15
    moveBullet = 0

    seconds = 15
    pygame.time.set_timer(USEREVENT, 1000)

    while True:
        bulletRect.x = (myShipX + myShipWidth / 2) - 3
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # quit pygame
                quit() # quit python

            elif event.type== USEREVENT:
                seconds -= 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveX = 6
                elif event.key == pygame.K_LEFT:
                    moveX = -6
                elif event.key == pygame.K_SPACE:
                    moveBullet = -8
                    myShipShootSound.play()

            elif event.type == pygame.KEYUP:
                moveX = 0

        screen.fill(white)
        #screen.blit(bgImage, (0, 0))

        # for i in range(2):
        #     for j in range(int(len(enemyList)/2)):
        #         screen.blit(enemyList[i], (enemyWidth * j, enemyHeight * i))

        screen.blit(enemyBullet, enemyBulletRect)
        for i in range(len(enemyList)):
            screen.blit(enemyShip, (enemyList[i].x, enemyList[i].y))

        screen.blit(bullet, bulletRect)
        screen.blit(myShip, (myShipX, myShipY))
        myShipRect = pygame.Rect(myShipX, myShipY, myShipWidth, myShipHeight)

        myShipX += moveX
        bulletRect.y += moveBullet
        enemyBulletRect.y += 5
        # print(enemyBulletRect.y)

        for i in range(len(enemyList)):
            if bulletRect.colliderect(enemyList[i]):
                enemyList.pop(i)
                bulletRect.y = myShipY + 15
                moveBullet = 0
                break

        if myShipRect.colliderect(enemyBulletRect):
            # print("collision")
            pass

        if myShipX > width - myShipWidth:
            moveX = 0
        elif myShipX < 0:
            moveX = 0

        if bulletRect.y < 0:
            bulletRect.y = myShipY + 15
            moveBullet = 0

        if enemyBulletRect.y > height:
            # pygame.time.delay(2000)
            randomEnemy = random.choice(enemyList)
            enemyBulletRect.x = randomEnemy.x + enemyWidth / 2
            enemyBulletRect.y = randomEnemy.bottom - 20
            enemyShootSound.play()

        showTimer(seconds)

        pygame.display.update()

 #game()
homeScreen()
