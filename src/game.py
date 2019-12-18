import sys
import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
screen = pygame.display.set_mode( (650, 600) )
character_speed = 5
x = 325
y = 500

while True:
    pygame.time.delay(100)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= character_speed

        if keys[pygame.K_RIGHT]:
            x += character_speed

        if keys[pygame.K_UP]:
            y -= character_speed

        if keys[pygame.K_DOWN]:
            y += character_speed

        screen.fill(black)
        pygame.draw.circle(screen, white, (x, y), 10)  
        pygame.display.update()