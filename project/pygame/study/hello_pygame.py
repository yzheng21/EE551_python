import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,500))
myfont = pygame.font.Font(None,60)
white = 255,255,255
blue = 0,0,200
textImage = myfont.render("Hello pygame",True,white)
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill(blue)
    screen.blit(textImage, (100, 100))
    pygame.display.update()