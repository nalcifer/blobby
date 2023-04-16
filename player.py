import pygame

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("img/kirby.png").convert_alpha()
        self.rect = self.image.get_rect(x=x, y=y)

    def draw(self,screen):
        screen.blit(self.image, self.rect)


