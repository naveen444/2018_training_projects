import pygame

pygame.init()

red = 255,0,0
black = 0,0,0
white = 255,255,255

width = 1000
height = 600

screen = pygame.display.set_mode((width,height))

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(white)
    pygame.display.update()