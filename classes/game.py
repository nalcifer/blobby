import pygame, time, random
from classes.blobby import *
from config.screen import *
from classes.background import *
from classes.object import *
from config.config import *
from pages.home import *



# Variables "globales"
background = Background(bg1_image,bg2_image,bg3_image, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, bg_speed)
current_player_sprite_good = 0

# Class principale de jeu
class Game:
  
  # Initialisation de la fênetre et de la boucle
  def __init__(self, screen):
    self.screen = screen
    self.running = True
  # Iniatialisation des variables de la class game 
  def var(self):
    # Variables plus generales (initialisation du temps / background) 
    self.clock = pygame.time.Clock()                              
    self.background = Background(bg1_image,bg2_image,bg3_image, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, bg_speed)
    self.prev_time = time.time()

    # Variables pour le player                       
    self.current_player_image = current_player_sprite_good
    self.time_between_animation = 0
    self.player_level = 4
    self.move_y = player_height
    self.number_sprite = 0

    # Variables pour avaler recracher
    self.objectInMouse = []
    self.lenObjectInMouse = len(self.objectInMouse)


  # Fonction pour les animations ( qui marche pas très bien pour le delay )  --> a corriger
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
      # config.screen
      redrawWindow()

      # Boucle pour calculer le delta time (temps entre deux frames)
      self.clock.tick(FPS)
      self.now = time.time()
      self.dt = self.now - self.prev_time
      self.prev_time = self.now


      # Boucle de gestion des evenements
      for event in pygame.event.get():
        # Permet de quitter la fenetre
        if event.type == pygame.QUIT:
          pygame.quit()
          run = False

        # events défini dans : config.config
        # boucle pour définir le spawn aléatoire de batiments et de consommables
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
      

      # Spawn des obstacles et des consommables
      for obstacle in obstacles:
        obstacle.posX -= self.dt * speed_level 
        if obstacle.posX < ( - SCREEN_WIDTH) :
          obstacles.pop(obstacles.index(obstacle))

        # gestions des collisions pour tous les obstacles / consommables
        if pygame.Rect.colliderect(obstacle.rect, player.rect) == True :
          # Si c'est un objet mortel alors fin de la partie
          if obstacle.collide == True :
            pygame.quit()
          
          # Si c'est un objet commestible, le joueur le prend dans sa bouche
          elif obstacle.collide == False and len(self.objectInMouse) == 0:
            self.objectInMouse.append(obstacle)
            obstacles.pop(obstacles.index(obstacle))
        
        # Teste des collisions en cas de recrachage de l'objet 
        for obstaclee in obstacles: 
          if pygame.Rect.colliderect(obstacle.rect, obstaclee.rect) == True and obstaclee != obstacle:
            print("aaaa")
            obstacles.pop(obstacles.index(obstaclee))
          for objects in objectsCaught:
            if pygame.Rect.colliderect(objects.rect, obstaclee.rect) == True and obstaclee.collide == False:
              print("bbbb")
              objectsCaught.pop(objectsCaught.index(objects))
              obstacles.pop(obstacles.index(obstaclee))

      # Mécanique d'avaler/recracher et de changement de difficulté
      if len(self.objectInMouse) == 1:
        for objects in self.objectInMouse:
          # Avaler
          if keyPlayer[pygame.K_SPACE]:
            if objects.good == False:
              self.objectInMouse.pop(self.objectInMouse.index(objects))
              
            elif objects.good == True:
              self.objectInMouse.pop(self.objectInMouse.index(objects))

          # Recracher
          elif keyPlayer[pygame.K_RSHIFT] :
            objectsCaught.append(objects)
            self.objectInMouse.pop(self.objectInMouse.index(objects))
            objects.posY = player.y

      # Boucle pour changer la vitesse du joueur en fonction de ce qu'il avale --> à revoir
      for objects in objectsCaught: 
        objects.posX += self.dt * ( bg_speed * 2 ) 
        if objects.posX >  SCREEN_WIDTH : 
          objectsCaught.pop(objectsCaught.index(objects))
          
      # Contrôle du joueur
      keyPlayer = pygame.key.get_pressed()
      for player in players:
        if keyPlayer[pygame.K_UP] and self.player.rect.y > 0:
          self.move_y -= self.player.speed * self.dt
        if keyPlayer[pygame.K_DOWN] and self.player.rect.y < (SCREEN_HEIGHT - 218):
          self.move_y += self.player.speed * self.dt
      

      # Animation du Blobby (idle)
      self.animation(player_image_good, self.current_player_image, self.dt, self.move_y)
      
      pygame.display.flip()
      pygame.display.update()