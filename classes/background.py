from config.screen import *
from config.config import *

class Background :
    # Initialisation des variables de Background
    def __init__(self, img1, img2, img3, posX, posY, screenWidth, screenHeight, speed, translateX=0):
        self.img1 = img1
        self.img2 = img2
        self.img3 = img3
        self.posX = posX
        self.posY = posY
        self.speed = speed
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.translateX = translateX
        
        self.nbr_bg = round(( SCREEN_WIDTH * 3 ) / bg1_width) + 1

    # Fonction pour dessiner le background
    def drawBg(self) :
        posXtemp = self.posX
        posXtemp = ( -posXtemp )
        for i in range(self.nbr_bg):
            screen.blit(self.img1, (posXtemp + (posXtemp + (i * SCREEN_HEIGHT * bg1_ratio)), self.posY))
            screen.blit(self.img2, (posXtemp + (posXtemp + (i * SCREEN_HEIGHT * bg1_ratio)), self.posY))
            screen.blit(self.img3, (posXtemp + (posXtemp + (i * SCREEN_HEIGHT * bg1_ratio)), self.posY))
            
    # Fonction pour initialiser le Background
    def initbg(self):
        for i in range(self.nbr_bg):
            bg.append(Background(self.img1, self.img2, self.img3, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, bg_speed))
            bg.append(Background(self.img1, self.img2, self.img3, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, bg_speed))
            bg.append(Background(self.img1, self.img2, self.img3, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, bg_speed))
