#! /usr/bin/env python
# coding:utf8

import pygame
import sys
import cv2

#path_string='~/MyFiles/MyMusic/'

music_name=sys.argv[1]

# print type(argv[1])

pygame.mixer.init()
track=pygame.mixer.music.load(music_name)
pygame.mixer.music.play()
cv2.namedWindow('Music')
music=cv2.imread('lena.jpg',1)
cv2.imshow('Music',music)
while True:
    if cv2.waitKey(0)==ord('q'):
        break
cv2.destroyAllWindows()
pygame.mixer.music.play()
