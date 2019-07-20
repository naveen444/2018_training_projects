import pygame

pygame.init()

red = 255,0,0
black = 0,0,0
white = 255,255,255

width = 1000
height = 600

screen = pygame.display.set_mode((width,height))
x = 0
y = 0

move_x = 0
move_y = 0

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 1
                move_y = 0
            elif event.key == pygame.K_LEFT:
                move_x = -1
                move_y = 0
            elif event.key == pygame.K_DOWN:
                move_y = 1
                move_x = 0
            elif event.key == pygame.K_UP:
                move_y = -1
                move_x = 0
        elif event.type == pygame.KEYUP:
            move_x = 0
            move_y = 0

    screen.fill(white)

    pygame.draw.rect(screen,red,[x,y,50,50])
    x += move_x
    y += move_y

    if x > width:
        x = -50
    elif y > height:
        y = -50
    elif x < -50:
        x = width
    elif y < -50:
        y = height

    pygame.display.update()