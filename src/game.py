import sys
import pygame

pygame.init()

screen = pygame.display.set_mode( (550, 700) )

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        
