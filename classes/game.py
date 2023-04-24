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
current_player_sprite_good = 0
rotate = 0

class Game:
  # Initialisation de la fênetre et de la boucle
  def __init__(self, screen):
    self.screen = screen
    self.running = True

  def var(self):
    self.clock = pygame.time.Clock()
    self.current_player_image = current_player_sprite_good
    self.background = Background(bg1_image,bg2_image,bg3_image, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, bg_speed)
    self.prev_time = time.time()
    self.time_between_animation = 0
    self.player_level = 4
    self.move_y = player_height
    self.number_sprite = 0

  def animation(self, list_anim, current_image, deltatime, y, time = 0.2):
      if time >= 0.2:
        self.number_sprite = (self.number_sprite + 1) % len(list_anim)
        current_image = list_anim[self.number_sprite]
        time = 0
      self.player = Player(current_image , player_width, y)
      self.player.initPlayer()
      time += deltatime


  # Fonction pour la boucle principale
  def run(self):
    while self.running:
      redrawWindow(rotate)


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
            obstacles.append(Object(building_image ,SCREEN_WIDTH, SCREEN_HEIGHT/2, collide = True, good = False))
          elif obstacle == 1:
            obstacles.append(Object(consumable_soda_img ,SCREEN_WIDTH, random.randrange(100000) % (SCREEN_HEIGHT - consumable_soda_height), collide = False, good = True))
          elif obstacle == 2:
            obstacles.append(Object(consumable_carrot_img ,SCREEN_WIDTH, random.randrange(100000) % (SCREEN_HEIGHT - consumable_carrot_height),  collide = False, good = False)) 
        
      # Déplacement du background en fonction du delta time 
      for bgs in bg: 
        bgs.posX = ( bgs.posX + (bg_speed * self.dt) ) % (SCREEN_HEIGHT * bg1_ratio)
      

      for objects in layerss: 
        objects.posX -= self.dt * (bg_speed * 2) 
        if objects.posX < ( - SCREEN_WIDTH) : # If our obstacle is off the screen we will remove it
          layerss.pop(layerss.index(objects))

        # Contrôle du joueur
      for obstacle in obstacles: 
        obstacle.posX -= self.dt * speed_level 
        if obstacle.posX < ( - SCREEN_WIDTH) : # If our obstacle is off the screen we will remove it
          obstacles.pop(obstacles.index(obstacle))
        if pygame.Rect.colliderect(obstacle.rect, player.rect) == True and obstacle.collide == True:
          pygame.quit()
        elif pygame.Rect.colliderect(obstacle.rect, player.rect) == True and obstacle.collide == False and obstacle.good == False:
          if self.player_level > 0:
            print("bad")
            self.player_level -= 1
            self.player.speed /= 1.2
          elif self.player_level >= 0:
            print("bad")
            self.player_level -= 1
          obstacles.pop(obstacles.index(obstacle))
          
        elif pygame.Rect.colliderect(obstacle.rect, player.rect) == True and obstacle.collide == False and obstacle.good == True:
          if self.player_level < 7:
            print("good")
            self.player_level += 1
            self.player.speed *= 1.2
          elif self.player_level <= 7:
            print("good")
            self.player_level += 1
          obstacles.pop(obstacles.index(obstacle))

      # Contrôle du joueur
      keyPlayer = pygame.key.get_pressed()
      for player in players:
        if keyPlayer[pygame.K_UP] and self.player.rect.y > 0:
          self.move_y -= self.player.speed * self.dt
        if keyPlayer[pygame.K_DOWN] and self.player.rect.y < (SCREEN_HEIGHT - 218):
          self.move_y += self.player.speed * self.dt
      
      self.animation(player_image_good, self.current_player_image, self.dt, self.move_y)
       
      pygame.display.flip()
      pygame.display.update()