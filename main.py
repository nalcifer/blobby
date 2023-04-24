import pygame
from classes.blobby import *
from config.screen import *
from classes.background import *
from classes.game import *
from classes.game import *

pygame.init() # Initialisation de pygame

game = Game(screen) # Variable pour le jeu 
game.var()


background.initbg()

run = home(font)
if run == True:
  game.run() # Debut de la boucle de jeu 

pygame.quit() # Quitter le jeu
