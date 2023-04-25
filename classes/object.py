import pygame
from config.config import *
from config.screen import *

# Class qui va être utiliser par tous les objets fixes de notre scene (consommables, batiments...)
class Object:
    # Initialisation des variables des Objects
    def __init__(self, img, posX, posY, collide, good, rectX=0, rectY=0):
        self.img = img
        self.posX = posX
        self.posY = posY
        if rectX == 0 :
            rectX = self.posX
        if rectY == 0 :
            rectY = self.posY
        self.rect = self.img.get_rect(x = rectX, y = rectY)  
        self.collide = collide
        self.good = good

    # Fonction qui dessine les objets
    def draw(self):
        screen.blit(self.img, (self.posX, self.posY))
        self.rect = self.img.get_rect(x = self.posX, y = self.posY)