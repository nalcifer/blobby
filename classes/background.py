from config.screen import *
from config.config import *

class Background :
    # Initialisation des variables de Background
    def __init__(self, img1, img2, img3, posX, posY, screenWidth, screenHeight, speed, translateX=0):
        self.img1 = img1
        self.img2 = img2
        self.img3 = img3
        self.posX1 = posX
        self.posX2 = posX
        self.posX3 = posX
        self.posY = posY
        self.speed = speed
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.translateX = translateX
        
        self.nbr_bg1 = int( SCREEN_WIDTH * 3 / bg1_width) + 1
        self.nbr_bg2 = int( SCREEN_WIDTH * 3 / bg2_width) + 2
        self.nbr_bg3 = int( SCREEN_WIDTH * 3 / bg3_width) + 1

    def update(self, dt):
        self.posX1 = ( self.posX1 + (self.speed * dt) ) % (bg1_width)
        self.posX2 = ( self.posX2 + (self.speed * dt) ) % (bg2_width)
        self.posX3 = ( self.posX3 + (self.speed * dt) ) % (bg3_width)

    # Fonction pour dessiner le background
    def drawBg(self) :
        posX1temp = self.posX1
        posX1temp = ( -posX1temp )
        
        posX2temp = self.posX2
        posX2temp = ( -posX2temp )
        
        posX3temp = self.posX3
        posX3temp = ( -posX3temp )

        for i in range(self.nbr_bg1):
            screen.blit(self.img1, (posX1temp + (posX1temp + (i * bg1_height)), self.posY))
        for i in range(self.nbr_bg2):
            screen.blit(self.img2, (posX2temp + (posX2temp + (i * bg2_width)), self.posY))
        for i in range(self.nbr_bg3):
            screen.blit(self.img3, (posX3temp + (posX3temp + (i * bg3_width)), 7 * SCREEN_HEIGHT / 8))
