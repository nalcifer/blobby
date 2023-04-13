import pygame
# import math
# from randomGeneration import *
from asset import *
from classes.background import *
from config import *

pygame.init()

clock = pygame.time.Clock()
FPS = 60



#define game variables
scroll = 0

ground_image = pygame.image.load("img/ground.png").convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()



bg_image = pygame.image.load("img/bg.png").convert_alpha()
bg_width = bg_image.get_width()
bg_height = bg_image.get_height()

background = Background(posX=0, posY=0, speed=0, img=bg_image)

# # fonction qui défini le background 
# def drawBg():
#   for x in range(15):
#     screen.blit(bg_image, ((x * bg_width) - scroll * 2.5, SCREEN_HEIGHT - bg_height))
    
# # fonction qui dessine le sol
# def drawGround():
#   for x in range(15):
#     screen.blit(ground_image, ((x * ground_width) - scroll * 2.5, SCREEN_HEIGHT - ground_height))

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

  clock.tick(FPS)

  # #draw world
  # drawBg()
  # drawGround()
  drawPlayer()

  # # inifinite background (of poor)
  # scroll += 3
  
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