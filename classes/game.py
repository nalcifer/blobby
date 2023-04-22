import pygame, time, random
from classes.blobby import *
from config.screen import *
from classes.background import *
from classes.object import *
from classes.layers import *
from config.config import *
from pages.home import *

# Class principales pour le jeu
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
    self.objectInMouse = []
    self.lenObjectInMouse = len(self.objectInMouse)

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
          obstacle = random.randrange(0,10)
          if obstacle == 0:
            obstacles.append(Object(tree_image ,SCREEN_WIDTH, SCREEN_HEIGHT/2, collide = True, good = False))
          elif obstacle == 1:
            obstacles.append(Object(consumables_bad_image ,SCREEN_WIDTH, random.randrange(100000) % SCREEN_HEIGHT, collide = False, good = False))
          elif obstacle == 2:
            obstacles.append(Object(consumables_good_image ,SCREEN_WIDTH, random.randrange(100000) % SCREEN_HEIGHT,  collide = False, good = True)) 
        
        objects = random.randrange(0,100)
        if objects == 0:
          layerss.append(Layers(building_image ,SCREEN_WIDTH, SCREEN_HEIGHT/3))

      # Déplacement du background en fonction du delta time 
      for bgs in bg: 
        bgs.posX = ( bgs.posX + (bg_speed * self.dt) ) % (SCREEN_HEIGHT * bg1_ratio)
      

      for objects in layerss: 
        objects.posX -= self.dt * (bg_speed / 2) 
        if objects.posX < ( - SCREEN_WIDTH) : # If our obstacle is off the screen we will remove it
          layerss.pop(layerss.index(objects))

        # Contrôle du joueur
      for obstacle in obstacles: 
        obstacle.posX -= self.dt * bg_speed 
        if obstacle.posX < ( - SCREEN_WIDTH) : # If our obstacle is off the screen we will remove it
          obstacles.pop(obstacles.index(obstacle))
        if pygame.Rect.colliderect(obstacle.rect, player.rect) == True :
          # Si c'est un obstacle mortel alors fin de la partie
          if obstacle.collide == True :
            pygame.quit()
          # Si c'est un element comestible
          elif obstacle.collide == False and len(self.objectInMouse) == 0:
            print("aaaaaaaaaa")
            self.objectInMouse.append(obstacle)
            obstacles.pop(obstacles.index(obstacle))


      print(len(self.objectInMouse))
      if len(self.objectInMouse) == 1:
        for objects in self.objectInMouse:
          if keyPlayer[pygame.K_SPACE]:
            if objects.good == False:
              print("bad")
              self.objectInMouse.pop(self.objectInMouse.index(objects))
              
            elif objects.good == True:
              print("good")
              self.objectInMouse.pop(self.objectInMouse.index(objects))


          elif keyPlayer[pygame.K_RSHIFT] :
            objectsCaught.append(objects)
            self.objectInMouse.pop(self.objectInMouse.index(objects))
            objects.posY = player.y






      for objects in objectsCaught: 
        objects.posX += self.dt * ( bg_speed * 2 ) 
        if objects.posX >  SCREEN_WIDTH : # If our obstacle is off the screen we will remove it
          objectsCaught.pop(objectsCaught.index(objects))


          
      # Contrôle du joueur
      keyPlayer = pygame.key.get_pressed()
      for player in players:
        if keyPlayer[pygame.K_UP] and self.player.rect.y > 0:
          player.y -= self.player.speed * self.dt
        if keyPlayer[pygame.K_DOWN] and self.player.rect.y < (SCREEN_HEIGHT - 218):
          player.y += self.player.speed * self.dt
       
      pygame.display.flip()
      pygame.display.update()