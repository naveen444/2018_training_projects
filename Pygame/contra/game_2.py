import pygame
import random
import os

WIDTH = 1000
HEIGHT = 480
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

class Spritesheet():

    def __init__(self, file_name):
        pygame.sprite.Sprite.__init__(self)
        self.spriteSheet = file_name

    def getImage(self, x, y, width, height):

        image = pygame.Surface((width, height))
        image.blit(self.spriteSheet, (0,0), (x, y, width, height))
        image.set_colorkey(YELLOW)

        return image

class Contra(pygame.sprite.Sprite):

    standingFrames = []
    kickFrames = []
    punchFrames = []
    walkingFrames = []
    superKick = []
    health = 500

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        spritesheet = Spritesheet(player_img)
        self.image = spritesheet.getImage(952,119,163,224)
        self.standingFrames.append(self.image)

        self.image = spritesheet.getImage(955,879,135,225)
        self.walkingFrames.append(self.image)
        self.image = spritesheet.getImage(1114,879,119,225)
        self.walkingFrames.append(self.image)
        self.image = spritesheet.getImage(1252,897,146,206)
        self.walkingFrames.append(self.image)
        self.image = spritesheet.getImage(1430,868,140,237)
        self.walkingFrames.append(self.image)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 + 250, HEIGHT / 2 + 90)
        self.pos = 0

        self.walkingFramesActive = False

    def update(self):
        self.pos += 5

        frame = (self.pos // 30) % len(self.standingFrames)
        self.image = self.standingFrames[frame]

        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_RIGHT]:
            self.walkingFramesActive = True
        else:
            self.walkingFramesActive = False

        if self.walkingFramesActive:
            frame = (self.pos // 50) % len(self.walkingFrames)
            self.image = self.walkingFrames[frame]

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

path = os.path.dirname(__file__)
# print(path)
img_folder = os.path.join(path,'assets')
# print(img_folder)
player_img = pygame.image.load(os.path.join(img_folder,'playersheet.png')).convert()
backgroundImage = pygame.image.load(os.path.join(img_folder,'bg.png')).convert()

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Contra()
bullets = pygame.sprite.Group()
all_sprites.add(player)

def camera(x,y=0):
    screen.blit(backgroundImage, (x,y))

# Game loop
running = True
x = 0
moveX = 0
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_RIGHT]:
        moveX = -5
    elif keystate[pygame.K_LEFT]:
        moveX = 0

    x += moveX
    # Update
    all_sprites.update()

    # Draw / render
    # screen.fill(BLACK)
    camera(x)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()