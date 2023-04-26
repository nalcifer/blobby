from config.screen import *
from config.config import *


class Player:
    # Fonction pour initialiser les variables de Blobby (joueur)
    def __init__(self, list_img_1, list_img_2, list_img_anim_1, list_img_anim_2, x, y):
        self.list_img_1 = list_img_1
        self.list_img_2 = list_img_2
        self.list_img_anim_1 = list_img_anim_1
        self.list_img_anim_2 = list_img_anim_2
        self.x = x
        self.y = y
        self.rect = self.list_img_1[0].get_rect(x=x, y=y)
        self.speed = 250
        self.anime_speed = 20
        self.current_sprite_player = 0 
        self.anim = False 
        self.current_anime_sprite_player = 0

    # Fonction pour dessiner Blobby
    def draw(self, dt, level, anime_eat):
        if anime_eat == False and self.current_anime_sprite_player >= (len(player_image_good_anim) - 1):
            self.current_anime_sprite_player = 0
        
        if anime_eat == True and self.current_anime_sprite_player < (len(player_image_good_anim) - 1):
            self.current_anime_sprite_player = (self.current_anime_sprite_player + dt * self.anime_speed)
            if level >= 4:    
                screen.blit(self.list_img_anim_1[int(self.current_anime_sprite_player)], (self.x, self.y))
                self.rect = self.list_img_anim_1[int(self.current_anime_sprite_player)].get_rect(x=self.x, y=self.y)
            else: 
                screen.blit(self.list_img_anim_2[int(self.current_anime_sprite_player)], (self.x, self.y))
                self.rect = self.list_img_anim_2[int(self.current_anime_sprite_player)].get_rect(x=self.x, y=self.y)
            self.current_sprite_player = 0
        else: 
            self.current_sprite_player = (self.current_sprite_player + dt * self.anime_speed) % len(player_image_good)
            if level >= 4:    
                screen.blit(self.list_img_1[int(self.current_sprite_player)], (self.x, self.y))
                self.rect = self.list_img_1[int(self.current_sprite_player)].get_rect(x=self.x, y=self.y)
            else: 
                screen.blit(self.list_img_2[int(self.current_sprite_player)], (self.x, self.y))
                self.rect = self.list_img_2[int(self.current_sprite_player)].get_rect(x=self.x, y=self.y)