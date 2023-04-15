import pygame
from config import *

class FixedObject: 
    def __init__(self, img, scaleX, scaleY, posX, posY):
        self.img = img
        self.posX = posX
        self.posY = posY
        self.scaleX = scaleX
        self.scaleY = scaleY


    def drawObject(self):
        screen.blit(self.img, (600, SCREEN_HEIGHT / 2))        

