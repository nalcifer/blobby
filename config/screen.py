import pygame

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blobby")



bg = []
layerss = []
obstacles = []
players = []
def redrawWindow(rotate):
    print(rotate)
    rotate += 1
    for bgs in bg: 
       bgs.drawBg()
    for objects in layerss:
        objects.draw()
    for obstacle in obstacles:
        obstacle.draw(rotate)
    for player in players:
        player.draw()
    pygame.display.update()