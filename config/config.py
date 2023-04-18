import pygame, random
from config.screen import *

#create game window
FPS = 60

bg_speed = 100


# -------- EVENT ----------
event1 = pygame.USEREVENT+1
event2 = pygame.USEREVENT+2

pygame.time.set_timer(event1, 500)
pygame.time.set_timer(event2, 3000)

pygame.time.set_timer(event2, random.randrange(2000, 3500)) # Will trigger every 2 - 3.5 seconds


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

# player
player_image = pygame.image.load("img/kirby.png").convert_alpha()
player_width = player_image.get_width()
player_height = player_image.get_height()
player_ratio = player_width/tree_height
player_width = (SCREEN_HEIGHT / 10) * tree_ratio
player_height = SCREEN_HEIGHT / 10

player_image = pygame.transform.scale(player_image, (player_width, player_height))