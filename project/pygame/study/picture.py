import pygame,math
from pygame.locals import *
import sys
pygame.init()
screen = pygame.display.set_mode((600,500))
color = 255,255,0
color1 = 255,0,255
position = 300,250
radius = 100
width = 10
blue = 0,0,200
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill(blue)
    pygame.draw.circle(screen,color,position,radius,width)
    pygame.draw.line(screen,color,(100,100),(500,400),width)
    pos = 200,150,200,200
    start_angle = math.radians(0)
    end_angle = math.radians(180)
    pygame.draw.arc(screen,color1,pos,start_angle,end_angle,width)
    pygame.display.update()