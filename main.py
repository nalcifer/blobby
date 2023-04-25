import pygame
from classes.blobby import *
from config.screen import *
from classes.background import *
from classes.game import *
from classes.game import *
from pages.score import *

pygame.init() # Initialisation de pygame

game = Game(screen) # Variable pour le jeu 
game.var()
run = home(font)
while run == True:

  score = game.run(run) # Debut de la boucle de jeu 
  while score != 0:
    run = EndScore(font, score)
    if run == True or run == False:
      score = 0
pygame.quit() # Quitter le jeu
