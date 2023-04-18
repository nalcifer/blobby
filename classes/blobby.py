import pygame
from config.screen import *
from config.config import *


class Player:
    def __init__(self, img, x, y):
        self.img = img
        self.x = x
        self.y = y
        self.rect = self.img.get_rect(x=x, y=y)
        self.speed = 250

    def draw(self):
        screen.blit(self.img, (self.x, self.y))


    def initPlayer(self):
        players.append(Player(player_image, player_width, player_height))