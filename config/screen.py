import pygame

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blobby")

bg = []
fixedObjects = []
obstacles = []
players = []
def redrawWindow():
    for bgs in bg: 
       bgs.drawBg()
    for objects in fixedObjects:
        objects.draw()
    for obstacle in obstacles:
        obstacle.draw()
    for player in players:
        player.draw()
    pygame.display.update()