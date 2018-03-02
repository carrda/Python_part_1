# PyGame Exercises

import sys
import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
x = 1
y = 1

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    x += 1
    y += 1
    screen.fill((0, 0, 0))
    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (x, y, 100, 100),
        0
        )
    pygame.display.update()


