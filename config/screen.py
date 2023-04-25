import pygame


# Définition de la fenetre
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blobby")
icon = pygame.image.load("img/logo.png")
pygame.display.set_icon(icon)


# Redessinage des éléments de la fenetre 
obstacles = []
objectsCaught = []
players = []
def redrawWindow(bg):
    bg.drawBg()
    
    for objectCaught in objectsCaught:
        objectCaught.draw()
    for obstacle in obstacles:
        obstacle.draw()
    for player in players:
        player.draw()