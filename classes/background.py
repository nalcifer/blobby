import pygame 
from config import *

class Background :
    def __init__(self, img, posX, posY, screenWidth, screenHeight, speed, translateX=0):
        self.img = img
        self.posX = posX
        self.posY = posY
        self.speed = speed
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.translateX = translateX

    def drawBg(self) :
        nbr_img = round(( SCREEN_WIDTH * 2 ) / bg_width) + 1
        for i in range(nbr_img):
            self.posX = 0
            screen.blit(self.img, (self.posX + (self.posX + (i * SCREEN_HEIGHT * bg_ratio)), self.posY))


    def update(self, deltaTime) : 
        self.translateX = ( self.translateX + (self.speed * deltaTime) ) % (SCREEN_HEIGHT * bg_ratio)
        nbr_img = round(( SCREEN_WIDTH * 2 ) / bg_width) + 1
        for i in range(nbr_img):
            screen.blit( self.img, ( - ( self.translateX - (i * SCREEN_HEIGHT * bg_ratio )) , self.posY ) )
            # if i == 0:
                # print(( self.translateX * (deltaTime * self.speed)) - (i * SCREEN_HEIGHT * bg_ratio ))



# 50 * 3 -> 150



    # def update(self, deltaTime) : 
    #     self.translateX = (( self.translateX + 1 ) * self.speed * deltaTime) % (SCREEN_HEIGHT * bg_ratio)
    #     print(self.translateX)
    #     nbr_img = round(( SCREEN_WIDTH * 2 ) / bg_width) + 1
        
    #     for i in range(1):
            
    #         self.posX = 0
            
    #         screen.blit( self.img, ( self.posX + (i * SCREEN_HEIGHT * bg_ratio ) - self.translateX, self.posY ) )
    #         # print( self.posX + (i * SCREEN_HEIGHT * bg_ratio ) - self.translateX )
            

            