import pygame
from player import *
from screen import *
from background import *
import time


# Class principale pour le jeu
class Game:
  # Initialisation de la fênetre et de la boucle
  def __init__(self, screen):
    self.screen = screen
    self.running = True
  
  def var(self):
    self.clock = pygame.time.Clock()
    self.FPS = 60
    self.dt = 0
    self.player = Player(200,251)
    self.background = Background()
    self.prev_time = time.time()


  # Fonction pour la boucle principale
  def run(self):
    scroll = self.dt
    while self.running:

      
      self.clock.tick(self.FPS)# DeltaTime

      self.now = time.time()

      self.dt = self.now - self.prev_time
      self.prev_time = self.now

      print(self.dt)


      self.background.drawbg(screen,scroll) #Fonction qui dessine le background

      self.player.draw(screen) # Fonction qui dessine le joueur

      scroll += self.player.speed * self.dt

      
      


      # Contrôle du joueur
      keyPlayer = pygame.key.get_pressed()
      if keyPlayer[pygame.K_UP] and self.player.rect.y > 0:
        self.player.rect.y -= self.player.speed * self.dt
      if keyPlayer[pygame.K_DOWN] and self.player.rect.y < (SCREEN_HEIGHT - 218):
        self.player.rect.y += self.player.speed * self.dt
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
      
      pygame.display.update()
      
pygame.init()# Initialisation de pygame



game = Game(screen) # Variable pour le jeu 

game.var()


game.run()# Debut de la boucle de jeu 


pygame.quit()# Fin de pygame 