import pygame
from config.screen import *
pygame.font.init()
# affiche une fenetre pour lancer le jeu
def home(font):
    # on récupère les boutons de la manette
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    #on initialise run False
    run = False
    while run == False:
        #on initialise my_text avec le rendu de la font importé en jaune avec le text press to start
        my_text = font.render('PRESS SPACE TO START ', True, 'yellow')
        #on affiche my_text au coordonées données
        screen.blit(my_text, (SCREEN_WIDTH/15, SCREEN_HEIGHT/1.5))
        # pour tout évenement pygame qui se déclenche
        for event in pygame.event.get():
            # on initialise keyP avec l'évenement une touche à été pressé
            keyP = pygame.key.get_pressed()
            #si la touche pressé est espace, on passe run true
            if keyP[pygame.K_SPACE]:
                run = True
                return run
            # si l'évenement est un bouton de manette baisé
            if event.type == pygame.JOYBUTTONDOWN:
                # et que c'est le bouton à la position 0 (X pour une PS4), on passe run true
                if pygame.joystick.Joystick(0).get_button(0):
                    run = True
                    return run
                #quitter
            if event.type == pygame.QUIT:
                run = True
        pygame.display.flip()







        # Je sais pas : Dorian si tu pouvais mettre des commentaires explicatifs stp :) (oui j'essayerais d'en mettre)