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
bg1_image = pygame.image.load("img/layer 1.png").convert_alpha()
bg1_width = bg1_image.get_width()
bg1_height = bg1_image.get_height()
bg1_ratio = bg1_width/bg1_height
bg1_image = pygame.transform.scale(bg1_image, ((SCREEN_HEIGHT * bg1_ratio), SCREEN_HEIGHT))

bg2_image = pygame.image.load("img/layer 2.png").convert_alpha()
bg2_width = bg2_image.get_width()
bg2_height = bg2_image.get_height()
bg2_ratio = bg2_width/bg2_height
bg2_image = pygame.transform.scale(bg2_image, ((SCREEN_HEIGHT * bg2_ratio), SCREEN_HEIGHT))

bg3_image = pygame.image.load("img/layer 3.png").convert_alpha()
bg3_width = bg3_image.get_width()
bg3_height = bg3_image.get_height()
bg3_ratio = bg3_width/bg3_height
bg3_image = pygame.transform.scale(bg3_image, ((SCREEN_HEIGHT * bg3_ratio), SCREEN_HEIGHT))




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