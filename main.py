import pygame, time
from asset import *
from classes.background import *
from config import *
from classes.fixedObject import *
from classes.generationaleatoire import *

pygame.init()

clock = pygame.time.Clock()
FPS = 60
SPEED = 100
prev_time = time.time()


background = Background(bg_image, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, SPEED)


obstacles = []
def redrawWindow():
  for obstacle in obstacles:
    obstacle.draw()
  pygame.display.update()

event1 = pygame.USEREVENT+1
event2 = pygame.USEREVENT+2

pygame.time.set_timer(event1, 500)
pygame.time.set_timer(event2, 3000)

pygame.time.set_timer(event2, random.randrange(2000, 3500)) # Will trigger every 2 - 3.5 seconds

#game loop
run = True
while run:
  redrawWindow()

  clock.tick(FPS)

  # gère le delta time
  now = time.time()
  deltaTime = now - prev_time
  prev_time = now

  # affiche le joueur
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      run = False

    if event.type == event2:
      r = random.randrange(0,2)
      if r == 0:
        obstacles.append(RandomGeneration(tree_image ,SCREEN_WIDTH, SCREEN_HEIGHT/2, 200, 200))



  for obstacle in obstacles: 
    obstacle.posX -= deltaTime * SPEED 
    if obstacle.posX < obstacle.posX * -1: # If our obstacle is off the screen we will remove it
      obstacles.pop(obstacles.index(obstacle))


  background.update(deltaTime)

  #event handlers
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()