import pygame
from config.screen import *
pygame.font.init()


#affiche le score durant la partie
def Score(font, score):
    my_text = font.render(str(score), True, 'Black')
    my_text_height = my_text.get_height()
    screen.blit(my_text, ( SCREEN_WIDTH / 8, SCREEN_HEIGHT - 1.2 * my_text_height))
    pygame.display.flip()

#affiche une fenetre en fin de partie avec le score et permettant de rejouer ou de quitter
def EndScore(font52,font100, score, best):
    #création de l'image
    bg1_image = pygame.image.load("img/ecran_mort.png").convert()
    #remeusure de la surface de l'image
    back = pygame.transform.scale(bg1_image, (SCREEN_WIDTH, SCREEN_HEIGHT) )
    #affichage du fond
    screen.blit(back, (0,0))
    #affichage des texte
    highscore = font52.render( "HIGHSCORE :" , True, 'red')
    screen.blit(highscore, (50,0))
    bestscore1 = font52.render( str(best[0]) +" : " + str(best[1]) , True, 'grey')
    screen.blit(bestscore1, (50,50))
    bestscore2 = font52.render( str(best[2]) + " : " + str(best[3]), True, 'grey')
    screen.blit(bestscore2, (50,100))
    bestscore3 = font52.render( str(best[4]) +" : " + str(best[5]), True, 'grey')
    screen.blit(bestscore3, (50,150))
    leave = font52.render( "QUIT (Q)", True, 'black')
    leave_width = leave.get_width()
    leave_height = leave.get_height()
    screen.blit(leave, (SCREEN_WIDTH - 1.25 * leave_width, SCREEN_HEIGHT - 1.5 * leave_height))
    restart = font52.render( "RESTART (R)", True, 'black')
    restart_width = restart.get_width()
    restart_height = restart.get_height()
    screen.blit(restart, ( 0.25 * restart_width ,SCREEN_HEIGHT - 1.5 * restart_height))

    my_text = font100.render( "Your Score -> " + str(score), True, 'yellow')
    screen.blit(my_text,(SCREEN_WIDTH/5, SCREEN_HEIGHT/1.5))
    for event in pygame.event.get():
        keyPlayer = pygame.key.get_pressed() 
        if keyPlayer[pygame.K_r] :
            #vide les éléments en jeu pour recommencer la partie si on appuie sur r
            ennemies.clear()
            obstacles.clear()
            objectsCaught.clear()
            player_level = 4
            return True
        if keyPlayer[pygame.K_q] :
            #arrete la partie si on appuie sur q
            return False
    pygame.display.flip()