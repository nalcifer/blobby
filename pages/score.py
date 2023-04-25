import pygame
from config.screen import *
pygame.font.init()

def Score(font, score):
    my_text = font.render('Score = '+ str(score), True, 'Black')
    screen.blit(my_text, (250,250))
    pygame.display.flip()

def EndScore(font, score):
    coucou = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT)) 
    pygame.draw.rect(screen, "black", coucou)
    my_text = font.render( "Your Score ->" + str(score), True, 'White')
    screen.blit(my_text, (500,350))
    for event in pygame.event.get():
        keyPlayer = pygame.key.get_pressed() 
        if keyPlayer[pygame.K_r] :
            players.clear()
            obstacles.clear()
            objectsCaught.clear()
            return True
        if keyPlayer[pygame.K_q] :
            return False
    pygame.display.flip()