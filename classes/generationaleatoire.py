import pygame
from config import *

class RandomGeneration:
    def __init__(self, img, posX, posY, width, height):
        self.img = img
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.rotateCount = 0
        self.vel = 1.4

    def draw(self):
        self.rect = self.img.get_rect(x = self.posX, y = self.posY)  # Defines the accurate hitbox for our character 
        pygame.draw.rect(screen, (255,0,0), self.rect, 2)
        screen.blit(self.img, (self.posX,self.posY))