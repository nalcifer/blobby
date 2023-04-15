import pygame, time
from asset import *
from classes.background import *
from config import *
from classes.fixedObject import *

pygame.init()

clock = pygame.time.Clock()
FPS = 300
prev_time = time.time()


#define game variables
scroll = 0
background = Background(bg_image, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 100)
# bg_image = pygame.transform.scale_by(pygame.image.load("img/bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))


tree = FixedObject(tree_image, 0, 0, 0, 0)

# background draw
background.drawBg()
# draw tree
tree.drawObject()

# position de player
playerPosX = 200
playerPosY = 200

# fonction qui dessine le player
def drawPlayer():
  player = pygame.Rect((playerPosX, playerPosY), (50, 50)) 
  colliderPlayer = pygame.draw.rect(screen, "red", player)
  return colliderPlayer 
speedPlayer = 7

drawTree(screen, scroll)

#game loop
run = True
while run:

  # gère les fps 
  clock.tick(FPS)
  # gère le delta time
  now = time.time()
  deltaTime = now - prev_time
  prev_time = now

  # affiche le joueur
  drawPlayer()

  # background scroll
  # background.update(deltaTime)



  colliderTree = drawTree(screen, scroll)
  colliderPlayer = drawPlayer()
  if pygame.Rect.colliderect(colliderTree, colliderPlayer) == True:
    run = False

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