import pygame
pygame.font.init()

def launch(screen, font):
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    run = False
    while run == False:
        my_text = font.render('Press Space to start ', True, 'white')
        screen.blit(my_text, (150,350))
        for event in pygame.event.get():
            keyP = pygame.key.get_pressed()
            if keyP[pygame.K_SPACE]:
                run = True
                return run
            if event.type == pygame.JOYBUTTONDOWN:
                if pygame.joystick.Joystick(0).get_button(0):
                    run = True
                    return run
            if event.type == pygame.QUIT:
                run = True
        pygame.display.flip()