# -*- coding: utf-8 -*-

import pygame
from random import randint
from sys import exit

pygame.init()

screen=pygame.display.set_mode((600,700),0,32)

pygame.display.set_caption("hello world!")

background=pygame.image.load('/home/mwn/lena.jpg').convert()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background,(randint(1,100),randint(1,100)))

    pygame.display.update()
