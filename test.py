import pygame
import math
# from randomGeneration import *
from asset import *
import time

pygame.init()

clock = pygame.time.Clock()
FPS = 60

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 432

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



#define game variables
scroll = 0

ground_image = pygame.image.load("img/ground.png").convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()



bg_image = pygame.image.load("img/bg.png").convert_alpha()
bg_width = bg_image.get_width()
bg_height = bg_image.get_height()


#def slime():
  #i = 0
  #slime = pygame.Rect((780, 0, 20, 20))
  #pygame.draw.rect(screen, "GREEN", slime)
  #pygame.display.flip
  #while i < 100:
   # time.sleep(0.050)
    #slime.y += 1
    #pygame.draw.rect(screen, "GREEN", slime)
    #pygame.display.flip
    #i += 1


# fonction qui défini le background 
def drawBg():
  for x in range(15):
    screen.blit(bg_image, ((x * bg_width) - scroll * 2.5, SCREEN_HEIGHT - bg_height))

skyPosX = 0
skyPosY = 0

def drawRectSky():
  surface = pygame.Surface((800, 50))
  sky = pygame.Rect((skyPosX, skyPosY), (800, 50))
  colliderSky = pygame.draw.rect(surface, "blue", sky, 1)
  return colliderSky
    



# fonction qui dessine le sol
def drawGround():
  for x in range(15):
    screen.blit(ground_image, ((x * ground_width) - scroll * 2.5, SCREEN_HEIGHT - ground_height))



groundPosX = 0
groundPosY = 369

def drawRectGround():
  surface2 = pygame.Surface((800, 63))
  ground = pygame.Rect((groundPosX, groundPosY), (800, 63))
  colliderGround = pygame.draw.rect(screen, "yellow", ground, 1)
  return colliderGround
    
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

  #draw world
  drawBg()
  drawGround()
  drawPlayer()
  #slime()

  # inifinite background (of poor)
  scroll += 2

  
    


  
  
  colliderTree = drawTree(screen, scroll)
  colliderPlayer = drawPlayer()
 

  if pygame.Rect.colliderect(colliderTree, colliderPlayer) == True:
    run = False

  colliderGround = drawRectGround()
  
  if pygame.Rect.colliderect(colliderGround, colliderPlayer) == True:
    if colliderPlayer.bottom > colliderGround.top:
      playerPosY -= speedPlayer
  
  colliderSky = drawRectSky()
  
  if pygame.Rect.colliderect(colliderSky, colliderPlayer) == True:
    if colliderPlayer.top < colliderSky.bottom:
      playerPosY += speedPlayer

  # get keypresses player
  keyPlayer = pygame.key.get_pressed()
  if keyPlayer[pygame.K_UP] and playerPosY > 0:
    print("ror")
    playerPosY -= speedPlayer
  if keyPlayer[pygame.K_DOWN] and playerPosY < ( SCREEN_HEIGHT - 50 )  :
    playerPosY += speedPlayer

  
  
    

  #event handlers
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()


pygame.quit()