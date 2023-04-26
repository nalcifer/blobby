import pygame
from classes.blobby import *
from config.screen import *
from config.database import *
from classes.background import *
from classes.game import *
from classes.game import *

pygame.init() # Initialisation de pygame

pygame.init() # Initialisation de pygame

game = Game(screen) # Variable pour le jeu 
game.var()
run = home(font100)
stop = 0
name = 'ENTER YOUR NAME'
while run == True:

  score = game.run(run) # Debut de la boucle de jeu 
  while stop == 0:# création d'une boucle pour récuperer le nom du joueur, valide ne appuyant sur espace
    name = enterName(font100, name)
    for event in pygame.event.get():
      keyP = pygame.key.get_pressed()
      if keyP[pygame.K_SPACE]:
          stop = 1
  best = database(score, name)# ajout des valeurs du joueurs à la bdd et inialise dans best
  while score != 0:
    run = EndScore(font52,font100, score, best) # affiche le score du joueur et le tableau des score
    if run == True or run == False:#permet de relancer une partie en fonction de run 
      score = 0
pygame.quit() # Quitter le jeu
