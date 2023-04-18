from config.screen import *
from config.config import *

class Background :
    def __init__(self, img, posX, posY, screenWidth, screenHeight, speed, translateX=0):
        self.img = img
        self.posX = posX
        self.posY = posY
        self.speed = speed
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.translateX = translateX
        
        self.nbr_bg = round(( SCREEN_WIDTH * 3 ) / bg_width) + 1

    def drawBg(self) :
        posXtemp = self.posX
        posXtemp = ( -posXtemp )
        for i in range(self.nbr_bg):
            screen.blit(self.img, (posXtemp + (posXtemp + (i * SCREEN_HEIGHT * bg_ratio)), self.posY))

    def initbg(self):
        for i in range(self.nbr_bg):
            bg.append(Background(bg_image, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, bg_speed))