import pygame
from config.config import *
from config.screen import *

# Class qui va être utiliser par tous les objets fixes de notre scene (consommables, batiments...)
class Object:
    # Initialisation des variables des Objects
    def __init__(self, img, posX, posY, collide, good, height = 0, width = 0):
        self.img = img
        self.posX = posX
        self.posY = posY
        self.height = height
        self.width = width
        self.rect = self.img.get_rect(x = self.posX, y = self.posY)  
        self.collide = collide
        self.good = good

    # Fonction qui dessine les objets avec collisions
    def draw(self):
        screen.blit(self.img, (self.posX, self.posY))
        self.rect = self.img.get_rect(x = self.posX, y = self.posY)
        pygame.Rect.inflate_ip(self.rect, -self.width, -self.height)
        #-- pygame.draw.rect(screen, (250,0,0), self.rect, 2)