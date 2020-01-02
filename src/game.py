import sys
import pygame

pygame.init()

moving = False
current_key = 0
white = (255, 255, 255)
black = (0, 0, 0)
screen = pygame.display.set_mode( (650, 600) )
character_speed = 15
x = 325
y = 500

while True:
    pygame.time.delay(50)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if keys[pygame.K_LSHIFT]:
            x -= character_speed - 5
        else:
            x -= character_speed
    if keys[pygame.K_RIGHT]:
        if keys[pygame.K_LSHIFT]:
            x += character_speed - 5
        else:
            x += character_speed
    if keys[pygame.K_UP]:
        if keys[pygame.K_LSHIFT]:
            y -= character_speed - 5
        else:
            y -= character_speed
    if keys[pygame.K_DOWN]:
        if keys[pygame.K_LSHIFT]:
            y += character_speed - 5
        else:
            y += character_speed

            
    screen.fill(black)
    pygame.draw.circle(screen, white, (x, y), 10)  
    pygame.display.update()