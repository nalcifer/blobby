import pygame


# Définition de la fenetre
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blobby")
icon = pygame.image.load("img/logo.png")
pygame.display.set_icon(icon)


# Redessinage des éléments de la fenetre 
ennemies = []
obstacles = []
objectsCaught = []
def redrawWindow(bg, player, dt, level, eat):
    bg.drawBg()
    for objectCaught in objectsCaught:
        objectCaught.draw()
    for obstacle in obstacles:
        obstacle.draw()
    for ennemie in ennemies:
        print("here")
        ennemie.draw(dt)
    player.draw(dt, level, eat)