import pygame


#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 432

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# ------- LOAD IMG --------
# background
bg_image = pygame.image.load("img/bg.png").convert_alpha()
bg_width = bg_image.get_width()
bg_height = bg_image.get_height()
bg_ratio = bg_width/bg_height
bg_image = pygame.transform.scale(bg_image, ((SCREEN_HEIGHT * bg_ratio), SCREEN_HEIGHT))

# fixed object
tree_image = pygame.image.load("img/tree.png").convert_alpha()
tree_width = tree_image.get_width()
tree_height = tree_image.get_height()
tree_ratio = tree_width/tree_height
tree_image = pygame.transform.scale(tree_image, ((SCREEN_HEIGHT / 2) * tree_ratio , SCREEN_HEIGHT / 2))

