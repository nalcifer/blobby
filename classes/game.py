import pygame, time, random
from classes.blobby import *
from config.screen import *
from classes.background import *
from classes.object import *
from config.config import *
from pages.home import *
from classes.ennemies import *



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
    self.number_sprite = 0
    self.time_between_frame = 0
    self.player = Player(player_image_good, player_image_bad, player_image_good_anim, player_image_bad_anim, player_width, player_height)
    self.anime_eat = False

    # Variables pour avaler recracher
    self.objectInMouse = []
    self.lenObjectInMouse = len(self.objectInMouse)
      

  # Fonction pour la boucle principale
  def run(self):
    while self.running:
      
      # Boucle pour calculer le delta time (temps entre deux frames)
      # self.clock.tick(FPS)
      self.now = time.time()
      self.dt = self.now - self.prev_time
      # print("fps:" + str(1/self.dt))
      self.prev_time = self.now


      # config.screen
      # Redessine les objets de la scene
      if len(self.objectInMouse) != 0:
        self.anime_eat = True
      else: 
        self.anime_eat = False
      redrawWindow(background, self.player, self.dt, self.player_level, self.anime_eat)


      # Boucle de gestion des evenements
      for event in pygame.event.get():
        # Permet de quitter la fenetre
        if event.type == pygame.QUIT:
          pygame.quit()
          run = False


        # events défini dans : config.config
        # boucle pour définir le spawn aléatoire de batiments et de consommables
        if event.type == event2:
          obstacle = random.randrange(0,8)
          if obstacle == 0:
            obstacles.append(Object(building_image ,SCREEN_WIDTH, 6*SCREEN_HEIGHT/14, collide = True, good = False))
          elif obstacle == 1:
            obstacles.append(Object(consumable_soda_img ,SCREEN_WIDTH, random.randrange(100000) % (SCREEN_HEIGHT - consumable_soda_height * 2), collide = False, good = True))
          elif obstacle == 2:
            obstacles.append(Object(consumable_carrot_img ,SCREEN_WIDTH, random.randrange(100000) % (SCREEN_HEIGHT - consumable_carrot_height * 2),  collide = False, good = False)) 
          elif obstacle == 3:
            obstacles.append(Object(building_image_two ,SCREEN_WIDTH, 3*SCREEN_HEIGHT/11, collide = True, good = False))
          elif obstacle == 4:
            # print("sheeeeeeeeeeeesh")
            ennemies.append(Ennemies(ennemie_image_bird, SCREEN_WIDTH, (SCREEN_HEIGHT / 8)))

      # Déplacement du background en fonction du delta time 
      background.update(self.dt)

      # Dépplacement des ennemies 
      for ennemie in ennemies: 
        ennemie.posX -= self.dt * speed_level
        if ennemie.posX < (- SCREEN_WIDTH) :
          ennemies.pop(ennemies.index(ennemie))

      # Spawn des obstacles et des consommables
      for obstacle in obstacles:
        obstacle.posX -= self.dt * speed_level 
        if obstacle.posX < ( - SCREEN_WIDTH) :
          obstacles.pop(obstacles.index(obstacle))

        # gestions des collisions pour tous les obstacles / consommables
        if pygame.Rect.colliderect(obstacle.rect, self.player.rect) == True :
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
            # print("aaaa")
            obstacles.pop(obstacles.index(obstaclee))
          for objects in objectsCaught:
            if pygame.Rect.colliderect(objects.rect, obstaclee.rect) == True and obstaclee.collide == False:
              # print("bbbb")
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
            objects.posY = self.player.y

      # Boucle pour changer la vitesse du joueur en fonction de ce qu'il avale --> à revoir
      for objects in objectsCaught: 
        objects.posX += self.dt * ( bg_speed * 2 ) 
        if objects.posX >  SCREEN_WIDTH : 
          objectsCaught.pop(objectsCaught.index(objects))
          
      # Contrôle du joueur
      keyPlayer = pygame.key.get_pressed()
      if keyPlayer[pygame.K_UP] and self.player.rect.y > 0:
        self.player.y -= self.player.speed * self.dt
      if keyPlayer[pygame.K_DOWN] and self.player.rect.y < (SCREEN_HEIGHT - player_height * 2):
        self.player.y += self.player.speed * self.dt

      pygame.display.update()