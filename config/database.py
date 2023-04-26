import pygame
import sqlite3
from config.screen import *
from pygame.locals import *
import time

baseDeDonnees = sqlite3.connect('contacts.db')
curseur = baseDeDonnees.cursor()
curseur.execute("CREATE TABLE IF NOT EXISTS joueurs (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL, score INTEGER NOT NULL)") # Création de la base de données
baseDeDonnees.commit() # On envoie la requête SQL

def database(score, name):
    best = []
    curseur.execute("INSERT INTO joueurs (name, score) VALUES (? , ?)", (name ,score)) # On ajoute un enregistrement
    baseDeDonnees.commit()
    curseur.execute("SELECT name,score FROM joueurs ORDER BY SCORE DESC")
    for contact in curseur.fetchall():
        best.append(contact[0])
        best.append(contact[1])
        print(contact)
    return best

def enterName(font, text):
        #curseur.execute("DELETE FROM joueurs WHERE id > 0") # On ajoute un enregistrement
        #baseDeDonnees.commit()
        bg1_image = pygame.image.load("img/ecran_mort.png").convert()
        back = pygame.transform.scale(bg1_image, (SCREEN_WIDTH, SCREEN_HEIGHT) )
        screen.blit(back, (0,0))
        name = font.render( text, True, 'yellow')
        rect = name.get_rect()
        rect.topleft = ((SCREEN_WIDTH/5, SCREEN_HEIGHT/1.5))
        cursor = Rect(rect.topright, (3, rect.height))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit
            
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(text)>0:
                        text =  text[:-1]
                else:
                    text += event.unicode
                img = font.render(text, True, 'yellow')
                rect.size=img.get_size()
                cursor.topleft = rect.topright
        screen.blit(name, rect)
        if time.time() % 1 > 0.5:
            pygame.draw.rect(screen, "yellow", cursor)
        pygame.display.update()

        return text
   