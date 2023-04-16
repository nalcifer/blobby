import pygame
from screen import *



class Background:
    def __init__(self):
        self.bg_image = pygame.image.load("img/bg.png").convert_alpha()
        self.bg_width = self.bg_image.get_width()
        self.bg_height = self.bg_image.get_height()
        self.scroll = 0
    
    def drawbg(self,screen,scroll):
        for x in range(15):
            screen.blit(self.bg_image, ((x * self.bg_width) - self.scroll * 2.5, SCREEN_HEIGHT - self.bg_height))
    

        