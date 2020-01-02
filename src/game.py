import sys
import pygame

pygame.init()

width = 756
height = 610
current_key = 0
white = (255, 255, 255)
black = (0, 0, 0)
screen = pygame.display.set_mode( (width, height) )
character_speed = 15
x = 228
y = 500

while True:
    pygame.time.delay(50)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x > 6:
            if keys[pygame.K_LSHIFT]:
                x -= round(character_speed / 2.5)
            else:
                x -= character_speed
    if keys[pygame.K_RIGHT]:
        if x < width / 1.6:
            if keys[pygame.K_LSHIFT]:
                x += round(character_speed / 2.5)
            else:
                x += character_speed
    if keys[pygame.K_UP]:
        if y > 12:
            if keys[pygame.K_LSHIFT]:
                y -= round(character_speed / 2.5)
            else:
                y -= character_speed
    if keys[pygame.K_DOWN]:
        if y < height - 10:
            if keys[pygame.K_LSHIFT]:
                y += round(character_speed / 2.5)
            else:
                y += character_speed

            
    screen.fill(black)
    pygame.draw.circle(screen, white, (x, y), 6)  
    pygame.display.update()