import pygame, random
from config.screen import *

#create game window
FPS = 60
bg_speed = 50
speed_level = 200

pygame.joystick.init()
pygame.font.init()
font = pygame.font.Font('font\SedgwickAveDisplay-Regular.ttf', 52)
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]


# -------- EVENT ----------
event1 = pygame.USEREVENT+1
event2 = pygame.USEREVENT+2

pygame.time.set_timer(event1, 100)
pygame.time.set_timer(event2, 3000)

pygame.time.set_timer(event2, random.randrange(500, 800)) # Will trigger every 2 - 3.5 seconds


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

# blobby good

image_player_type = pygame.image.load("img/blobby/blobby_bad_1.png").convert_alpha()
player_width = image_player_type.get_width()
player_height = image_player_type.get_height()
player_ratio = player_width/player_height
player_width = SCREEN_HEIGHT/6 * player_ratio
player_height = SCREEN_HEIGHT/6


player_image_good = []
player_image_good.append(pygame.transform.scale(pygame.image.load("img/blobby/blobby_good_1.png").convert_alpha(), (player_width, player_height)))
player_image_good.append(pygame.transform.scale(pygame.image.load("img/blobby/blobby_good_2.png").convert_alpha(), (player_width, player_height)))
player_image_good.append(pygame.transform.scale(pygame.image.load("img/blobby/blobby_good_3.png").convert_alpha(), (player_width, player_height)))
player_image_good.append(pygame.transform.scale(pygame.image.load("img/blobby/blobby_good_4.png").convert_alpha(), (player_width, player_height)))
player_image_good.append(pygame.transform.scale(pygame.image.load("img/blobby/blobby_good_5.png").convert_alpha(), (player_width, player_height)))

        
# blobby bad


player_image_bad = []
player_image_bad.append(pygame.transform.scale(pygame.image.load("img/blobby/blobby_bad_1.png").convert_alpha(), (player_width, player_height)))
player_image_bad.append(pygame.transform.scale(pygame.image.load("img/blobby/blobby_bad_2.png").convert_alpha(), (player_width, player_height)))
player_image_bad.append(pygame.transform.scale(pygame.image.load("img/blobby/blobby_bad_3.png").convert_alpha(), (player_width, player_height)))
player_image_bad.append(pygame.transform.scale(pygame.image.load("img/blobby/blobby_bad_4.png").convert_alpha(), (player_width, player_height)))
player_image_bad.append(pygame.transform.scale(pygame.image.load("img/blobby/blobby_good_5.png").convert_alpha(), (player_width, player_height)))



# fixed object
building_image = pygame.image.load("img/batiment 1.png").convert_alpha()
building_witdh = building_image.get_width()
building_height = building_image.get_height()
building_ratio = building_witdh/building_height
building_witdh = 3*SCREEN_HEIGHT/5 * building_ratio
building_height = 3*SCREEN_HEIGHT/4
building_image = pygame.transform.scale(building_image, (building_witdh, building_height))

# # Consumables carrot
# consumable_carrot_list = []
# consumable_carrot_list.append(pygame.image.load("img/consumables/carrot/carrot1.png").convert_alpha())
# consumable_carrot_list.append(pygame.image.load("img/consumables/carrot/carrot2.png").convert_alpha())
# consumable_carrot_list.append(pygame.image.load("img/consumables/carrot/carrot3.png").convert_alpha())
# consumable_carrot_list.append(pygame.image.load("img/consumables/carrot/carrot4.png").convert_alpha())
# consumable_carrot_list.append(pygame.image.load("img/consumables/carrot/carrot5.png").convert_alpha())
# consumable_carrot_list.append(pygame.image.load("img/consumables/carrot/carrot6.png").convert_alpha())
# consumable_carrot_list.append(pygame.image.load("img/consumables/carrot/carrot7.png").convert_alpha())
# consumable_carrot_list.append(pygame.image.load("img/consumables/carrot/carrot8.png").convert_alpha())

# # Consumables soda
# consumable_soda_list = []
# consumable_soda_list.append(pygame.image.load("img/consumables/soda/soda1.png").convert_alpha())
# consumable_soda_list.append(pygame.image.load("img/consumables/soda/soda2.png").convert_alpha())
# consumable_soda_list.append(pygame.image.load("img/consumables/soda/soda3.png").convert_alpha())
# consumable_soda_list.append(pygame.image.load("img/consumables/soda/soda4.png").convert_alpha())
# consumable_soda_list.append(pygame.image.load("img/consumables/soda/soda5.png").convert_alpha())
# consumable_soda_list.append(pygame.image.load("img/consumables/soda/soda6.png").convert_alpha())
# consumable_soda_list.append(pygame.image.load("img/consumables/soda/soda7.png").convert_alpha())
# consumable_soda_list.append(pygame.image.load("img/consumables/soda/soda8.png").convert_alpha())



# Carrot
consumable_soda_img = pygame.image.load("img/consumables/carrot/carrot1.png").convert_alpha()
consumable_soda_width = consumable_soda_img.get_width()
consumable_soda_height = consumable_soda_img.get_height()
consumable_soda_ratio = consumable_soda_width/consumable_soda_height
consumable_soda_width = SCREEN_HEIGHT/8 * consumable_soda_ratio
consumable_soda_height = SCREEN_HEIGHT/8
consumable_soda_img = pygame.transform.scale(consumable_soda_img, (consumable_soda_width, consumable_soda_height))

# Soda
consumable_carrot_img = pygame.image.load("img/consumables/soda/soda1.png").convert_alpha()
consumable_carrot_width = consumable_carrot_img.get_width()
consumable_carrot_height = consumable_carrot_img.get_height()
consumable_carrot_ratio = consumable_carrot_width/consumable_carrot_height
consumable_carrot_width = SCREEN_HEIGHT/8 * consumable_carrot_ratio
consumable_carrot_height = SCREEN_HEIGHT/8
consumable_carrot_img = pygame.transform.scale(consumable_carrot_img, (consumable_carrot_width, consumable_carrot_height))








# consumables_good_witdh = consumables_good_image.get_width()
# consumables_good_height = consumables_good_image.get_height()
# consumables_good_ratio = consumables_good_witdh/consumables_good_height
# consumables_good_witdh = SCREEN_HEIGHT/8 * consumables_good_ratio
# consumables_good_height = SCREEN_HEIGHT/8
# consumables_good_image = pygame.transform.scale(consumables_good_image, (consumables_good_witdh, consumables_good_height))


# consumables_bad_witdh = consumables_bad_image.get_width()
# consumables_bad_height = consumables_bad_image.get_height()
# consumables_bad_ratio = consumables_bad_witdh/consumables_bad_height
# consumables_bad_witdh = SCREEN_HEIGHT/8 * consumables_bad_ratio
# consumables_bad_height = SCREEN_HEIGHT/8
# consumables_bad_image = pygame.transform.scale(consumables_bad_image, (consumables_bad_witdh, consumables_bad_height))
