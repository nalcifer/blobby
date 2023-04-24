import pygame
from config.config import *
from config.screen import *

class Object:
    def __init__(self, img, posX, posY, collide, good):
        self.img = img
        self.posX = posX
        self.posY = posY
        self.rect = self.img.get_rect(x = self.posX, y = self.posY)  # Defines the accurate hitbox for our character 
        self.collide = collide
        self.good = good


    def draw(self):
        screen.blit(self.img, (self.posX, self.posY))
        self.rect = self.img.get_rect(x = self.posX, y = self.posY)