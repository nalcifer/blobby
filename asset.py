import pygame 
from random import *

pygame.init()

def drawTree(screen, scroll):
        scroll *= 2.5
        posTree = (900 - scroll)
        tree = pygame.Rect((posTree, 225), (50, 200)) 
        colliderTree = pygame.draw.rect(screen, "white", tree)
        return colliderTree
