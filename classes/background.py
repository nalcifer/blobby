import pygame 

class Background :
    def __init__(self, img, posX, posY, screenWidth, screenHeight, speed):
        self.img = img
        self.posX = posX
        self.posY = posY
        self.speed = speed
        self.screenWidht = screenWidth
        self.screenHeight = screenHeight

    