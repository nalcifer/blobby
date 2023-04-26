import pygame


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
pygame.display.set_caption("Blobby")
icon = pygame.image.load("img/logo.png")
pygame.display.set_icon(icon)


# Définition de la fenetre
SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()


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
        ennemie.draw(dt)
    player.draw(dt, level, eat)