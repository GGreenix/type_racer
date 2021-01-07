import pygame

pygame.init()

dim = (1000,550)
title = "tic tac toe"
run = True

canvas = pygame.display.set_mode(dim)

pygame.display.set_caption(title)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()