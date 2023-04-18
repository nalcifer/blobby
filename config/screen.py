import pygame

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


obstacles = []
bg = []
def redrawWindow():
    for bgs in bg: 
       bgs.drawBg()
    for obstacle in obstacles:
      obstacle.draw()
    pygame.display.update()
