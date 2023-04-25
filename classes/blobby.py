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
        self.current_sprite_player = 0 
        self.anim = False 
        self.number_of_frame = 0

    # Fonction pour dessiner Blobby
    def draw(self, dt, level, anime_eat):
        self.current_sprite_player += (dt / 0.15) 
        if self.current_sprite_player > 5:
            self.current_sprite_player = 0
            # print(anim, anime_eat)
        if anime_eat == False and self.anim == False:
            if level >= 4:    
                screen.blit(self.list_img_1[int(self.current_sprite_player)], (self.x, self.y))
                self.rect = self.list_img_1[int(self.current_sprite_player)].get_rect(x=self.x, y=self.y)
            else: 
                screen.blit(self.list_img_2[int(self.current_sprite_player)], (self.x, self.y))
                self.rect = self.list_img_2[int(self.current_sprite_player)].get_rect(x=self.x, y=self.y)
        else:
            self.anim = True
            if level >= 4:    
                screen.blit(self.list_img_anim_1[int(self.current_sprite_player)], (self.x, self.y))
                self.rect = self.list_img_anim_1[int(self.current_sprite_player)].get_rect(x=self.x, y=self.y)
                self.number_of_frame+=1
            else: 
                screen.blit(self.list_img_anim_2[int(self.current_sprite_player)], (self.x, self.y))
                self.rect = self.list_img_anim_2[int(self.current_sprite_player)].get_rect(x=self.x, y=self.y)
                self.number_of_frame+=1
            # print(self.number_of_frame)
            
            if self.number_of_frame >= len(self.list_img_anim_1):
                # print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                self.anim = False