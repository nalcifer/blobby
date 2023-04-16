import pygame
from pygame.locals import *
from player import *
from screen import *
from background import *
import time

# Initialisation des variables
clock = pygame.time.Clock()

prev_time = time.time()

FPS = 100

dt = 0


player = Player(200,251) # Création du joueur
background = Background() # Création du background

# Class principale pour le jeu
class Game:
  # Initialisation de la fênetre et de la boucle
  def __init__(self, screen):
    self.screen = screen
    self.running = True
    self.scroll = 0

  

  # Fonction pour la boucle principale
  def run(self):
    while self.running:

      

      background.drawbg(screen,self.scroll) #Fonction qui dessine le background

      player.draw(screen) # Fonction qui dessine le joueur

      self.scroll += 3

      # Contrôle du joueur
      keyPlayer = pygame.key.get_pressed()
      if keyPlayer[pygame.K_UP] and player.rect.y > 0:
        player.rect.y -= player.speed * dt
      if keyPlayer[pygame.K_DOWN] and player.rect.y < (SCREEN_HEIGHT - 218):
        player.rect.y += player.speed * dt
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
      
      pygame.display.update()
      
pygame.init()# Initialisation de pygame


game = Game(screen) # Variable pour le jeu 

clock.tick(FPS)

now = time.time()

dt = now - prev_time
prev_time = now# DeltaTime


game.run()# Debut de la boucle de jeu 


pygame.quit()# Fin de pygame 