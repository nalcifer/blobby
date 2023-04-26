import pygame
from config.config import *
from config.screen import *


# Class pour les ennemies
class Ennemies:
    # Initialisation des variables des Objects
    def __init__(self, img, posX, posY, rectX=0, rectY=0):
        self.img = img
        self.posX = posX
        self.posY = posY
        if rectX == 0 :
            rectX = self.posX
        if rectY == 0 :
            rectY = self.posY
        self.rect = self.img[0].get_rect(x = rectX, y = rectY)  
        self.current_ennemie_sprite = 0
        self.anime_speed = 20

    # Fonction qui dessine les objets
    def draw(self, dt):
        self.current_ennemie_sprite = (self.current_ennemie_sprite + dt * self.anime_speed) % len(ennemie_image_bird)
        screen.blit(self.img[int(self.current_ennemie_sprite)], (self.posX, self.posY))
        self.rect = self.img[int(self.current_ennemie_sprite)].get_rect(x = self.posX, y = self.posY)




