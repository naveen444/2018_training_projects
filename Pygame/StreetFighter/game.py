import pygame
from pygame.locals import *
from os import path


WIDTH = 1200
HEIGHT = 600
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'sounds')

class Spritesheet():

    def __init__(self, file_name):
        pygame.sprite.Sprite.__init__(self)
        self.spriteSheet = file_name

    def getImage(self, x, y, width, height):

        image = pygame.Surface((width, height))
        image.blit(self.spriteSheet, (0,0), (x, y, width, height))
        image.set_colorkey(BLACK)

        return image


class Player_1(pygame.sprite.Sprite):

    standingFrames = []
    kickFrames = []
    punchFrames = []
    walkingFrames = []
    superKick = []
    health = 500

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        spritesheet = Spritesheet(ken_sprite)
        self.image = spritesheet.getImage(48,247,106,239)
        self.standingFrames.append(self.image)
        self.image = spritesheet.getImage(264,240,113,249)
        self.standingFrames.append(self.image)
        self.image = spritesheet.getImage(482,248,106,237)
        self.standingFrames.append(self.image)
        self.image = spritesheet.getImage(687,247,112,241)
        self.standingFrames.append(self.image)

        self.image = spritesheet.getImage(42, 247, 116, 243)
        self.walkingFrames.append(self.image)
        self.image = spritesheet.getImage(44, 731, 118, 243)
        self.walkingFrames.append(self.image)
        self.image = spritesheet.getImage(256, 731, 118, 243)
        self.walkingFrames.append(self.image)

        self.image = spritesheet.getImage(42, 490, 118, 240)
        self.punchFrames.append(self.image)
        self.image = spritesheet.getImage(260, 489, 166, 240)
        self.punchFrames.append(self.image)
        self.image = spritesheet.getImage(472, 487, 122, 245)
        self.punchFrames.append(self.image)

        self.image = spritesheet.getImage(250, 1451, 118, 250)
        self.kickFrames.append(self.image)
        self.image = spritesheet.getImage(428, 1457, 208, 248)
        self.kickFrames.append(self.image)
        self.image = spritesheet.getImage(676, 1461, 120, 244)
        self.kickFrames.append(self.image)

        self.image = spritesheet.getImage(18, 1701, 116, 248)
        self.superKick.append(self.image)
        self.image = spritesheet.getImage(212, 1705, 172, 240)
        self.superKick.append(self.image)
        self.image = spritesheet.getImage(426, 1707, 216, 238)
        self.superKick.append(self.image)
        self.image = spritesheet.getImage(658, 1737, 188, 210)
        self.superKick.append(self.image)
        self.image = spritesheet.getImage(898, 1727, 118, 218)
        self.superKick.append(self.image)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 - 250, HEIGHT / 2 + 70)
        self.pos = 0

        self.moveX = 0

        self.walkingFramesActive = False
        self.punchActive = False
        self.kickActive = False
        self.superKickActive = False

    def update(self):
        self.pos += 5

        frame = (self.pos // 30) % len(self.standingFrames)
        # print("Position",self.pos//30)
        # print("Frame",frame)
        self.image = self.standingFrames[frame]

        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_RIGHT]:
            self.walkingFramesActive = True
        elif keystate[pygame.K_LEFT]:
            self.moveX = -5
            self.walkingFramesActive = True
        elif keystate[pygame.K_SPACE]:
            self.punchActive = True
        elif keystate[pygame.K_m]:
            self.kickActive = True
        else:
            self.walkingFramesActive = False
            self.punchActive = False
            self.kickActive = False
            self.moveX = 0

        self.rect.x += self.moveX

        self.hit = pygame.sprite.groupcollide(kenSprite, ryuSprite, False, False)
        # if self.hit:
        #     print("collision")

        if self.walkingFramesActive:
            frame = (self.pos // 30) % len(self.walkingFrames)
            self.image = self.walkingFrames[frame]
            self.moveX = 5
        elif self.punchActive:
            frame = (self.pos // 30) % len(self.punchFrames)
            self.image = self.punchFrames[frame]
        elif self.kickActive:
            frame = (self.pos // 30) % len(self.kickFrames)
            self.image = self.kickFrames[frame]


class Player_2(pygame.sprite.Sprite):

    standingFrames = []
    kick_frames = []
    punch_frames = []
    walking_frames = []
    super_kick_frames = []
    hit_frames = []
    health = 500

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        spritesheet = Spritesheet(ryu_sprite)
        self.image = spritesheet.getImage(2959,41,105,228)
        self.standingFrames.append(self.image)
        self.image = spritesheet.getImage(2751,38,99,230)
        self.standingFrames.append(self.image)
        self.image = spritesheet.getImage(2557,34,104,236)
        self.standingFrames.append(self.image)
        self.image = spritesheet.getImage(2358,40,108,228)
        self.standingFrames.append(self.image)

        self.image = spritesheet.getImage(2750, 41, 102, 226)
        self.walking_frames.append(self.image)
        self.image = spritesheet.getImage(2756, 317, 110, 224)
        self.walking_frames.append(self.image)
        self.image = spritesheet.getImage(2394, 315, 94, 226)
        self.walking_frames.append(self.image)

        self.image = spritesheet.getImage(2737, 1219, 130, 238)
        self.punch_frames.append(self.image)
        self.image = spritesheet.getImage(2492, 1213, 184, 240)
        self.punch_frames.append(self.image)
        self.image = spritesheet.getImage(2492, 1213, 184, 240)
        self.punch_frames.append(self.image)
        self.image = spritesheet.getImage(2300, 1219, 130, 236)
        self.punch_frames.append(self.image)
        self.image = spritesheet.getImage(2108, 1225, 112, 232)
        self.punch_frames.append(self.image)

        self.image = spritesheet.getImage(1012, 905, 94, 228)
        self.kick_frames.append(self.image)
        self.image = spritesheet.getImage(811, 878, 135, 252)
        self.kick_frames.append(self.image)

        self.image = spritesheet.getImage(58, 217, 96, 267)
        self.super_kick_frames.append(self.image)
        self.image = spritesheet.getImage(216, 260, 136, 219)
        self.super_kick_frames.append(self.image)
        self.image = spritesheet.getImage(394, 332, 212, 118)
        self.super_kick_frames.append(self.image)
        self.image = spritesheet.getImage(646, 282, 92, 200)
        self.super_kick_frames.append(self.image)
        self.image = spritesheet.getImage(806, 365, 180, 111)
        self.super_kick_frames.append(self.image)
        self.image = spritesheet.getImage(1026, 300, 98, 258)
        self.super_kick_frames.append(self.image)

        self.image = spritesheet.getImage(1174, 1571, 144, 242)
        self.hit_frames.append(self.image)
        self.image = spritesheet.getImage(1375, 1583, 123, 226)
        self.hit_frames.append(self.image)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2 + 250, HEIGHT / 2 + 90)
        self.pos = 0

        self.moveX = 0

        self.walkingFramesActive = False
        self.punchActive = False
        self.kickActive = False
        self.superKickActive = False
        self.isHit = False

    def update(self):
        self.pos += 5

        frame = (self.pos // 30) % len(self.standingFrames)
        # print("Position",self.pos//30)
        # print("Frame",frame)
        self.image = self.standingFrames[frame]

        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_d]:
            self.walkingFramesActive = True
        elif keystate[pygame.K_a]:
            self.moveX = -5
            self.walkingFramesActive = True
        elif keystate[pygame.K_s]:
            self.punchActive = True
        elif keystate[pygame.K_x]:
            self.kickActive = True
        else:
            self.walkingFramesActive = False
            self.punchActive = False
            self.kickActive = False
            self.moveX = 0

        self.rect.x += self.moveX

        self.hit = pygame.sprite.groupcollide(ryuSprite, kenSprite, False, False)
        # if self.hit:
        #     print("collision")

        if self.walkingFramesActive:
            frame = (self.pos // 30) % len(self.walking_frames)
            self.image = self.walking_frames[frame]
            self.moveX = 5
        elif self.punchActive:
            frame = (self.pos // 30) % len(self.punch_frames)
            self.image = self.punch_frames[frame]
        elif self.kickActive:
            frame = (self.pos // 30) % len(self.kick_frames)
            self.image = self.kick_frames[frame]

        if ken.punchActive or ken.kickActive:
            if self.hit:
                self.isHit = True
                self.health -= 5
        if ken.punchActive:
            if self.hit:
                self.isHit = True
                self.health -= 10

        if self.isHit:
            frame = (self.pos // 30) % len(self.hit_frames)
            self.image = self.hit_frames[frame]
            self.isHit = False
            punchSound.play()

pygame.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Street Fighter")
clock = pygame.time.Clock()

backgroundMusic = pygame.mixer.Sound(path.join(snd_dir, "StreetFighter.ogg"))
backgroundMusic.play(-1)

punchSound = pygame.mixer.Sound(path.join(snd_dir, "punch2.wav"))

ken_sprite = pygame.image.load(path.join(img_dir, "ken_.png")).convert_alpha()
ryu_sprite = pygame.image.load(path.join(img_dir, "ryu_.png")).convert_alpha()
background = pygame.image.load(path.join(img_dir, "background_1.jpg")).convert_alpha()

all_sprites = pygame.sprite.Group()
ken = Player_1()
ryu = Player_2()
all_sprites.add(ken)
all_sprites.add(ryu)

kenSprite = pygame.sprite.Group()
kenSprite.add(ken)
ryuSprite = pygame.sprite.Group()
ryuSprite.add(ryu)


def kenHealth():
    health = ken.health

    if health > 300:
        color = GREEN
    elif health > 200 and health < 300:
        color = YELLOW
    else:
        color = RED

    pygame.draw.rect(screen, color, [10,10,health,50])

def ryuHealth():
    health = ryu.health

    if health > 300:
        color = GREEN
    elif health > 200 and health < 300:
        color = YELLOW
    else:
        color = RED

    if health <= 0:
        health = 0

    pygame.draw.rect(screen, color, [WIDTH - 510, 10, health, 50])

def showTimer(secondsLeft):
    font = pygame.font.Font('font_1.ttf', 80)
    text = font.render(str(secondsLeft), True, RED)
    screen.blit(text, (WIDTH/2 - 40,10))

# Game loop
running = True
secondsLeft = 40
pygame.time.set_timer(USEREVENT, 1000)
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == USEREVENT:
            secondsLeft -= 1

    # Update
    all_sprites.update()

    # Draw / render
    # screen.fill(BLACK)
    screen.blit(background,(0,0))
    all_sprites.draw(screen)
    kenHealth()
    ryuHealth()
    showTimer(secondsLeft)
    pygame.display.flip()

pygame.quit()