import pygame, random
from config.screen import *

# Variables "globales"
FPS = 60
bg_speed = 50
speed_level = 200

# Initialisation des manettes
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
# Initialisation de la police
pygame.font.init()
font52 = pygame.font.Font('font\MCKLB___.ttf', 52)
font100 = pygame.font.Font('font\MCKLB___.ttf', 100)

# -------- EVENT ----------
event1 = pygame.USEREVENT+1
event2 = pygame.USEREVENT+2
event3 = pygame.USEREVENT+3

pygame.time.set_timer(event1, 100)
pygame.time.set_timer(event2, 3000)
pygame.time.set_timer(event3, 30000)

pygame.time.set_timer(event2, random.randrange(500, 800)) 

# ------- LOAD IMG --------
# background
bg1_image = pygame.image.load("img/layer 1.png").convert()
bg1_width = bg1_image.get_width()
bg1_height = bg1_image.get_height()
bg1_ratio = bg1_width/bg1_height
bg1_width = SCREEN_HEIGHT * bg1_ratio
bg1_height = SCREEN_HEIGHT 
bg1_image = pygame.transform.scale(bg1_image, ((SCREEN_HEIGHT * bg1_ratio), SCREEN_HEIGHT))

bg2_image = pygame.image.load("img/layer 2.png").convert_alpha()
bg2_width = bg2_image.get_width()
bg2_height = bg2_image.get_height()
bg2_ratio = bg2_width/bg2_height
bg2_width = SCREEN_HEIGHT * bg2_ratio
bg2_height = SCREEN_HEIGHT 
bg2_image = pygame.transform.scale(bg2_image, ((SCREEN_HEIGHT * bg2_ratio), SCREEN_HEIGHT))

bg3_image = pygame.image.load("img/layer 3.png").convert_alpha()
bg3_width = bg3_image.get_width()
bg3_height = bg3_image.get_height()
bg3_ratio = bg3_width/bg3_height
bg3_width = SCREEN_HEIGHT * bg3_ratio / 10
bg3_height = SCREEN_HEIGHT / 10
bg3_image = pygame.transform.scale(bg3_image, ((SCREEN_HEIGHT * bg3_ratio) / 8, SCREEN_HEIGHT / 8))


# Blobby : définition de la taille du joueur dans la scène
image_player_type = pygame.image.load("img/blobby/blobby_bad_1.png").convert_alpha()
player_width = image_player_type.get_width()
player_height = image_player_type.get_height()
player_ratio = player_width/player_height
player_width = SCREEN_HEIGHT/6 * player_ratio
player_height = SCREEN_HEIGHT/6

# blobby good
player_image_good = []
player_image_good.append(pygame.transform.scale(pygame.image.load("img/blobby/blobby_good_1.png").convert_alpha(), (player_width, player_height)))
player_image_good.append(pygame.transform.scale(pygame.image.load("img/blobby/blobby_good_2.png").convert_alpha(), (player_width, player_height)))
player_image_good.append(pygame.transform.scale(pygame.image.load("img/blobby/blobby_good_3.png").convert_alpha(), (player_width, player_height)))
player_image_good.append(pygame.transform.scale(pygame.image.load("img/blobby/blobby_good_4.png").convert_alpha(), (player_width, player_height)))
player_image_good.append(pygame.transform.scale(pygame.image.load("img/blobby/blobby_good_5.png").convert_alpha(), (player_width, player_height)))

# animation
player_image_good_anim = []
player_image_good_anim.append(pygame.transform.scale(pygame.image.load("img/blobby_feature/blobby good anim 1.png").convert_alpha(), (player_width, player_height)))
player_image_good_anim.append(pygame.transform.scale(pygame.image.load("img/blobby_feature/blobby good anim 2.png").convert_alpha(), (player_width, player_height)))
player_image_good_anim.append(pygame.transform.scale(pygame.image.load("img/blobby_feature/blobby good anim 3.png").convert_alpha(), (player_width, player_height)))
player_image_good_anim.append(pygame.transform.scale(pygame.image.load("img/blobby_feature/blobby good anim 4.png").convert_alpha(), (player_width, player_height)))
player_image_good_anim.append(pygame.transform.scale(pygame.image.load("img/blobby_feature/blobby good anim 5.png").convert_alpha(), (player_width, player_height)))
player_image_good_anim.append(pygame.transform.scale(pygame.image.load("img/blobby_feature/blobby good anim 6.png").convert_alpha(), (player_width, player_height)))
player_image_good_anim.append(pygame.transform.scale(pygame.image.load("img/blobby_feature/blobby good anim 7.png").convert_alpha(), (player_width, player_height)))
player_image_good_anim.append(pygame.transform.scale(pygame.image.load("img/blobby_feature/blobby good anim 8.png").convert_alpha(), (player_width, player_height)))
player_image_good_anim.append(pygame.transform.scale(pygame.image.load("img/blobby_feature/blobby good anim 9.png").convert_alpha(), (player_width, player_height)))
        
        
# blobby bad
player_image_bad = []
player_image_bad.append(pygame.transform.scale(pygame.image.load("img/blobby/blobby_bad_1.png").convert_alpha(), (player_width, player_height)))
player_image_bad.append(pygame.transform.scale(pygame.image.load("img/blobby/blobby_bad_2.png").convert_alpha(), (player_width, player_height)))
player_image_bad.append(pygame.transform.scale(pygame.image.load("img/blobby/blobby_bad_3.png").convert_alpha(), (player_width, player_height)))
player_image_bad.append(pygame.transform.scale(pygame.image.load("img/blobby/blobby_bad_4.png").convert_alpha(), (player_width, player_height)))
player_image_bad.append(pygame.transform.scale(pygame.image.load("img/blobby/blobby_bad_5.png").convert_alpha(), (player_width, player_height)))

# animation
player_image_bad_anim = []
player_image_bad_anim.append(pygame.transform.scale(pygame.image.load("img/blobby_feature/blobby bad anim 1.png").convert_alpha(), (player_width, player_height)))
player_image_bad_anim.append(pygame.transform.scale(pygame.image.load("img/blobby_feature/blobby bad anim 2.png").convert_alpha(), (player_width, player_height)))
player_image_bad_anim.append(pygame.transform.scale(pygame.image.load("img/blobby_feature/blobby bad anim 3.png").convert_alpha(), (player_width, player_height)))
player_image_bad_anim.append(pygame.transform.scale(pygame.image.load("img/blobby_feature/blobby bad anim 4.png").convert_alpha(), (player_width, player_height)))
player_image_bad_anim.append(pygame.transform.scale(pygame.image.load("img/blobby_feature/blobby bad anim 5.png").convert_alpha(), (player_width, player_height)))
player_image_bad_anim.append(pygame.transform.scale(pygame.image.load("img/blobby_feature/blobby bad anim 6.png").convert_alpha(), (player_width, player_height)))
player_image_bad_anim.append(pygame.transform.scale(pygame.image.load("img/blobby_feature/blobby bad anim 7.png").convert_alpha(), (player_width, player_height)))
player_image_bad_anim.append(pygame.transform.scale(pygame.image.load("img/blobby_feature/blobby bad anim 8.png").convert_alpha(), (player_width, player_height)))
player_image_bad_anim.append(pygame.transform.scale(pygame.image.load("img/blobby_feature/blobby good anim 9.png").convert_alpha(), (player_width, player_height)))
   

# fixed object
building_image = pygame.image.load("img/batiment 1.png").convert_alpha()
building_witdh = building_image.get_width()
building_height = building_image.get_height()
building_ratio = building_witdh/building_height
building_witdh = SCREEN_HEIGHT/2 * building_ratio
building_height = SCREEN_HEIGHT/2
building_image = pygame.transform.scale(building_image, (building_witdh, building_height))

building_image_two = pygame.image.load("img/batiment 2.png").convert_alpha()
building_witdh_two = building_image_two.get_width()
building_height_two = building_image_two.get_height()
building_ratio_two = building_witdh_two/building_height_two
building_witdh_two = 3*SCREEN_HEIGHT/5 * building_ratio_two
building_height_two = 3*SCREEN_HEIGHT/5
building_image_two = pygame.transform.scale(building_image_two, (building_witdh_two, building_height_two))

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

# Ennemies
image_bird_type = pygame.image.load("img/ennemies/bird_1.png").convert_alpha()
bird_width = image_bird_type.get_width()
bird_height = image_bird_type.get_height()
bird_ratio = bird_width/bird_height
bird_width = SCREEN_HEIGHT/6 * bird_ratio
bird_height = SCREEN_HEIGHT/6


ennemie_image_bird = []
ennemie_image_bird.append(pygame.transform.scale(pygame.image.load("img/ennemies/bird_1.png").convert_alpha(), (bird_width, bird_height)))
ennemie_image_bird.append(pygame.transform.scale(pygame.image.load("img/ennemies/bird_2.png").convert_alpha(), (bird_width, bird_height)))
ennemie_image_bird.append(pygame.transform.scale(pygame.image.load("img/ennemies/bird_3.png").convert_alpha(), (bird_width, bird_height)))
ennemie_image_bird.append(pygame.transform.scale(pygame.image.load("img/ennemies/bird_4.png").convert_alpha(), (bird_width, bird_height)))
ennemie_image_bird.append(pygame.transform.scale(pygame.image.load("img/ennemies/bird_5.png").convert_alpha(), (bird_width, bird_height)))
ennemie_image_bird.append(pygame.transform.scale(pygame.image.load("img/ennemies/bird_6.png").convert_alpha(), (bird_width, bird_height)))
ennemie_image_bird.append(pygame.transform.scale(pygame.image.load("img/ennemies/bird_7.png").convert_alpha(), (bird_width, bird_height)))


# pollution level
pollution_image_type = pygame.image.load("img/pollution/pollution_level_4.png").convert_alpha()
pollution_level_witdh = pollution_image_type.get_width()
pollution_level_height = pollution_image_type.get_height()
pollution_level_ratio = pollution_level_witdh / pollution_level_height
pollution_level_witdh = SCREEN_HEIGHT * pollution_level_ratio / 20
pollution_level_height = SCREEN_HEIGHT / 20

pollution_image = []
pollution_image.append(pygame.transform.scale(pygame.image.load("img/pollution/pollution_level_1.png").convert_alpha(), (pollution_level_witdh, pollution_level_height)))
pollution_image.append(pygame.transform.scale(pygame.image.load("img/pollution/pollution_level_2.png").convert_alpha(), (pollution_level_witdh, pollution_level_height)))
pollution_image.append(pygame.transform.scale(pygame.image.load("img/pollution/pollution_level_3.png").convert_alpha(), (pollution_level_witdh, pollution_level_height)))
pollution_image.append(pygame.transform.scale(pygame.image.load("img/pollution/pollution_level_4.png").convert_alpha(), (pollution_level_witdh, pollution_level_height)))
pollution_image.append(pygame.transform.scale(pygame.image.load("img/pollution/pollution_level_5.png").convert_alpha(), (pollution_level_witdh, pollution_level_height)))
pollution_image.append(pygame.transform.scale(pygame.image.load("img/pollution/pollution_level_6.png").convert_alpha(), (pollution_level_witdh, pollution_level_height)))
pollution_image.append(pygame.transform.scale(pygame.image.load("img/pollution/pollution_level_7.png").convert_alpha(), (pollution_level_witdh, pollution_level_height)))
pollution_image.append(pygame.transform.scale(pygame.image.load("img/pollution/pollution_level_8.png").convert_alpha(), (pollution_level_witdh, pollution_level_height)))
pollution_image.append(pygame.transform.scale(pygame.image.load("img/pollution/pollution_level_9.png").convert_alpha(), (pollution_level_witdh, pollution_level_height)))
