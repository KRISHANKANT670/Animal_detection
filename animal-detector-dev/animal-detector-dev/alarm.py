# modules used:

import pygame
from pygame.locals import *
from pygame import mixer

# Screen size :

pygame.init()
width = 1000
height = 500
window = pygame.display.set_mode((width,height))

# background image :

bg_img = pygame.image.load('C://Users//admin//Desktop//animal-detector-dev//animal-detector-dev//pri.png')
bg_img = pygame.transform.scale(bg_img,(width,height))

# Music import :

mixer.init()
mixer.music.load('C://Users//admin//Desktop//animal-detector-dev//animal-detector-dev//kk.wav')
mixer.music.play()

# looping for game :

runing = True
while runing:
    
    window.blit(bg_img,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            runing = False
    pygame.display.update()
pygame.quit()
