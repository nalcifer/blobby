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



background = Background(bg_image, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 3)
# bg_image = pygame.transform.scale_by(pygame.image.load("img/bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))

background.drawBg()
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