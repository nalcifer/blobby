import pygame
from config.config import *
from config.screen import *

class RandomGeneration:
    def __init__(self, img, posX, posY, width, height):
        self.img = img
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height

    def draw(self):
        self.rect = self.img.get_rect(x = self.posX, y = self.posY)  # Defines the accurate hitbox for our character 
        screen.blit(self.img, (self.posX,self.posY))