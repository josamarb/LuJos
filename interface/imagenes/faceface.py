import pygame
from pygame.locals import *
import time

pygame.init()

load = pygame.display.set_mode((1366, 768))
logo = pygame.image.load("LOGO.png")

clock = pygame.time.Clock()

pygame.display.flip()
while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()
    load.fill((255, 255, 255))
    load.blit(logo,(0,0))
    pygame.display.update()
    clock.tick(60)
