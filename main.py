import pygame, time
from asset import *
from classes.background import *
from config import *
from classes.fixedObject import *

pygame.init()

clock = pygame.time.Clock()
FPS = 60
prev_time = time.time()


background = Background(bg_image, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 100)
# bg_image = pygame.transform.scale_by(pygame.image.load("img/bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
tree = FixedObject(tree_image, ((SCREEN_HEIGHT / 2) * tree_ratio), SCREEN_HEIGHT / 2, SCREEN_WIDTH + 100, SCREEN_HEIGHT / 2, 300)
ground = FixedObject(tree_image, ((SCREEN_HEIGHT / 2) * tree_ratio), SCREEN_HEIGHT / 2, SCREEN_WIDTH + 100, SCREEN_HEIGHT / 2, 200)
# background draw
# background.drawBg()
# draw tree
# position de player
playerPosX = 200
playerPosY = 200

# fonction qui dessine le player
def drawPlayer():
  player = pygame.Rect((playerPosX, playerPosY), (50, 50)) 
  colliderPlayer = pygame.draw.rect(screen, "red", player)
  return colliderPlayer 
speedPlayer = 7


#game loop
run = True
while run:


  clock.tick(FPS)

  # gère le delta time
  now = time.time()
  deltaTime = now - prev_time
  prev_time = now

  # affiche le joueur
  
  background.update(deltaTime)
  
  ground.generateObject()
  tree.generateObject()
  ground.update(deltaTime)
  tree.update(deltaTime)
  drawPlayer()



  
  # get keypresses player
  keyPlayer = pygame.key.get_pressed()
  if keyPlayer[pygame.K_UP] and playerPosY > 0:
    playerPosY -= speedPlayer
  if keyPlayer[pygame.K_DOWN] and playerPosY < ( SCREEN_HEIGHT - 50 )  :
    playerPosY += speedPlayer

  
  
    

  #event handlers
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()