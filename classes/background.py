import pygame 
from config import screen

class Background :
    def __init__(self, img, posX, posY, screenWidth, screenHeight, speed):
        self.img = img
        self.posX = posX
        self.posY = posY
        self.speed = speed
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

    def drawBg(self):
        screen.blit(self.img, (self.posX, self.posY))