import pygame
from config.screen import *
pygame.font.init()


#affiche le scoredurant la partie
def Score(font, score):
    my_text = font.render('Score = '+ str(score), True, 'Black')
    screen.blit(my_text, (0,0))
    pygame.display.flip()

#affiche une fenetre en fin de partie avec le score et permettant de rejouer ou de quitter
def EndScore(font52,font100, score, best):
    bg1_image = pygame.image.load("img/ecran_mort.png").convert()
    back = pygame.transform.scale(bg1_image, (SCREEN_WIDTH, SCREEN_HEIGHT) )
    screen.blit(back, (0,0))
    highscore = font52.render( "HIGHSCORE :" , True, 'yellow')
    screen.blit(highscore, (50,0))
    bestscore1 = font52.render( str(best[0]) +" : " + str(best[1]) , True, 'red')
    screen.blit(bestscore1, (50,50))
    bestscore2 = font52.render( str(best[2]) + " : " + str(best[3]), True, 'pink')
    screen.blit(bestscore2, (50,100))
    bestscore3 = font52.render( str(best[4]) +" : " + str(best[5]), True, 'orange')
    screen.blit(bestscore3, (50,150))

    my_text = font100.render( "Your Score -> " + str(score), True, 'yellow')
    screen.blit(my_text,(SCREEN_WIDTH/5, SCREEN_HEIGHT/1.5))
    for event in pygame.event.get():
        keyPlayer = pygame.key.get_pressed() 
        if keyPlayer[pygame.K_r] :
            ennemies.clear()
            obstacles.clear()
            objectsCaught.clear()
            return True
        if keyPlayer[pygame.K_q] :
            return False
    pygame.display.flip()