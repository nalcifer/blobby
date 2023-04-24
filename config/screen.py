import pygame


# Définition de la fenetre
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blobby")


# Redessinage des éléments de la fenetre 
bg = []
obstacles = []
objectsCaught = []
players = []
def redrawWindow():
    for bgs in bg: 
       bgs.drawBg()
    for objectCaught in objectsCaught:
        objectCaught.draw()
    for obstacle in obstacles:
        obstacle.draw()
    for player in players:
        player.draw()
    pygame.display.update()