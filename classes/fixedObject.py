import pygame, random 
from config import *


class FixedObject: 
    def __init__(self, img, scaleX, scaleY, posX, posY, speed):
        self.img = img
        self.posX = posX
        self.posY = posY
        self.posXDefault = posX
        self.rect = self.img.get_rect(x = self.posX, y = self.posY)
        self.scaleX = scaleX
        self.scaleY = scaleY
        self.speed = speed
        self.randomGeneration = 0
        self.translateX = 0


    def drawObject(self):
        screen.blit(self.img, (600, SCREEN_HEIGHT / 2))        

    # update qui se lance à chaque frame
    def update(self, deltaTime):
        if self.posXDefault > -400: 
            print(self.posXDefault)
            self.posXDefault -= (deltaTime * self.speed)
            self.rect.move_ip( - (deltaTime * self.speed)  , 0)
        else: 
            pygame.Rect.update(self.rect, (self.posX, self.posY), (self.scaleX, self.scaleY))
            self.posXDefault = random.randrange(900, 2200)

    def generateObject(self):
        screen.blit(self.img, self.rect)
            