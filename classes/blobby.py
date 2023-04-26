import pygame
from config.screen import *
from config.config import *


class Player:
    # Fonction pour initialiser les variables de Blobby (joueur)
    def __init__(self, img, x, y):
        self.img = img
        self.x = x
        self.y = y
        self.rect = self.img.get_rect(x=x, y=y)
        self.speed = 250
        
        
    # Fonction pour dessiner Blobby
    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        self.rect = self.img.get_rect(x=self.x, y=self.y)

    # Fonction pour initialiser Blobby
    def initPlayer(self):
        if len(players)!= 0:
            del players[0]
        players.append(Player(self.img, self.x, self.y))

    # Fonction pour initialiser la gestion du score de la pollution 
    def avale_carotte(self):
        self.pollution_score += 1

    def avale_soda(self):
        self.pollution_score -= 1
