import sys
import pygame

#initializes the program
pygame.init()

#if statement has no purpose other than being able to store large amounts of variables
if True:
    width = 756
    height = 610
    current_key = 0
    white = (255, 255, 255)
    black = (0, 0, 0)
    pink = (186, 9, 115)
    purple = (83, 11, 122)
    screen = pygame.display.set_mode( (width, height) )
    character_speed = 10
    x = 231
    y = 500
    power = 1
    score = 0

#game starts the main loop
while True:
    #game delays the reading of the code so its not too fast when it runs
    pygame.time.delay(30)

    for event in pygame.event.get():
        #exits game when pygame.quit is called
        if event.type == pygame.QUIT:
            sys.exit()


    # if statement contains the code for player movement and border collision
    if True:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if keys[pygame.K_RIGHT]:
                if x > 36:
                    if keys[pygame.K_LSHIFT]:
                        x -= 2 * round(character_speed / 2)
                    else:
                        x -= 2 * character_speed
            else:
                if x > 36:
                    if keys[pygame.K_LSHIFT]:
                        x -= round(character_speed / 2)
                    else:
                        x -= character_speed
        if keys[pygame.K_RIGHT]:
            if x < width / 1.6 + 10:
                    if keys[pygame.K_LSHIFT]:
                        x += round(character_speed / 2)
                    else:
                        x += character_speed
        if keys[pygame.K_UP]:
            if y > 20:
                if keys[pygame.K_LSHIFT]:
                    y -= round(character_speed / 2)
                else:
                    y -= character_speed
        if keys[pygame.K_DOWN]:
            if y < height - 20:
                if keys[pygame.K_LSHIFT]:
                    y += round(character_speed / 2)
                else:
                    y += character_speed



    screen.fill(pink)
    pygame.draw.circle(screen, white, (x, y), 5)
    pygame.draw.rect(screen, purple, (round(width / 1.6) + 20, 0, width - width / 2, height))
    pygame.draw.rect(screen, purple, (0, 0, width, 15))
    pygame.draw.rect(screen, purple, (0, height - 15, width, 20))
    pygame.draw.rect(screen, purple, (0, 0, 30, height))
    pygame.display.update()