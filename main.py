import pygame, time, random
from classes.blobby import *
from config.screen import *
from classes.background import *
from game import *

pygame.init()# Initialisation de pygame

game = Game(screen) # Variable pour le jeu 
game.var()

player.initPlayer()
background.initbg()

run = home(font)
if run == True:
  game.run() # Debut de la boucle de jeu 

pygame.quit() # Quitter le jeu
