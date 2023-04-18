import pygame, time, random
from classes.blobby import *
from config.screen import *
from classes.background import *
from classes.generationaleatoire import *
from classes.fixedObject import *
from config.config import *

# Class principale pour le jeu
background = Background(bg_image, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, bg_speed)

class Game:
  # Initialisation de la fênetre et de la boucle
  def __init__(self, screen):
    self.screen = screen
    self.running = True

  

  def var(self):
    self.clock = pygame.time.Clock()
    self.player = Player(200,251)
    self.background = Background(bg_image, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, bg_speed)
    self.prev_time = time.time()


  # Fonction pour la boucle principale
  def run(self):
    while self.running:
      redrawWindow()

      
      self.clock.tick(FPS)# DeltaTime

      self.now = time.time()

      self.dt = self.now - self.prev_time
      self.prev_time = self.now

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          run = False

        if event.type == event2:
          r = random.randrange(0,2)
          if r == 0:
            obstacles.append(RandomGeneration(tree_image ,SCREEN_WIDTH, SCREEN_HEIGHT/2, 200, 200))
          
      for bgs in bg: 
        bgs.posX = ( bgs.posX + (bg_speed * self.dt) ) % (SCREEN_HEIGHT * bg_ratio)
      for obstacle in obstacles: 
        obstacle.posX -= self.dt * bg_speed 
        if obstacle.posX < obstacle.posX * -1: # If our obstacle is off the screen we will remove it
          obstacles.pop(obstacles.index(obstacle))


      self.player.draw(screen) # Fonction qui dessine le joueur

      

      # Contrôle du joueur
      keyPlayer = pygame.key.get_pressed()
      if keyPlayer[pygame.K_UP] and self.player.rect.y > 0:
        self.player.rect.y -= self.player.speed * self.dt
      if keyPlayer[pygame.K_DOWN] and self.player.rect.y < (SCREEN_HEIGHT - 218):
        self.player.rect.y += self.player.speed * self.dt
      pygame.display.update()
      
pygame.init()# Initialisation de pygame



game = Game(screen) # Variable pour le jeu 

game.var()

background.initbg()
game.run()# Debut de la boucle de jeu 


pygame.quit()# Fin de pygame 
