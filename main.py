import pygame, time, random
from classes.blobby import *
from config.screen import *
from classes.background import *
from classes.generationaleatoire import *
from classes.fixedObject import *
from config.config import *
from pages.home import *

# Class principale pour le jeu
background = Background(bg1_image,bg2_image,bg3_image, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, bg_speed)
player = Player(player_image , player_width, player_height)



class Game:
  # Initialisation de la fênetre et de la boucle
  def __init__(self, screen):
    self.screen = screen
    self.running = True

  

  def var(self):
    self.clock = pygame.time.Clock()
    self.player = Player(player_image , player_width, player_height)
    self.background = Background(bg1_image,bg2_image,bg3_image, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, bg_speed)
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
          obstacle = random.randrange(0,2)
          if obstacle == 0:
            obstacles.append(RandomGeneration(tree_image ,SCREEN_WIDTH, SCREEN_HEIGHT/2))
      
        objects = random.randrange(0,200)
        if objects == 0:
          fixedObjects.append(FixedObject(building_image ,SCREEN_WIDTH, SCREEN_HEIGHT/3))


      for bgs in bg: 
        bgs.posX = ( bgs.posX + (bg_speed * self.dt) ) % (SCREEN_HEIGHT * bg1_ratio)
      

      for objects in fixedObjects: 
        objects.posX -= self.dt * (bg_speed / 2) 
        if objects.posX < ( - SCREEN_WIDTH) : # If our obstacle is off the screen we will remove it
          objects.pop(objects.index(fixedObjects))
        # Contrôle du joueur

      for obstacle in obstacles: 
        obstacle.posX -= self.dt * bg_speed 
        if obstacle.posX < ( - SCREEN_WIDTH) : # If our obstacle is off the screen we will remove it
          obstacles.pop(obstacles.index(obstacle))
        # Contrôle du joueur

      keyPlayer = pygame.key.get_pressed()
      for player in players:
        if keyPlayer[pygame.K_UP] and self.player.rect.y > 0:
          player.y -= self.player.speed * self.dt
        if keyPlayer[pygame.K_DOWN] and self.player.rect.y < (SCREEN_HEIGHT - 218):
          player.y += self.player.speed * self.dt
          

       
      pygame.display.flip()
      pygame.display.update()
      
pygame.init()# Initialisation de pygame



game = Game(screen) # Variable pour le jeu 

game.var()



player.initPlayer()
background.initbg()

run = home(font)
if run == True:
  game.run()# Debut de la boucle de jeu 


pygame.quit()# Fin de pygame 
