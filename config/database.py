import pygame
import sqlite3 
from config.screen import *
from pygame.locals import *
import time

#création d'une bdd avec sqlite3
baseDeDonnees = sqlite3.connect('contacts.db')
curseur = baseDeDonnees.cursor()
curseur.execute("CREATE TABLE IF NOT EXISTS joueurs (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL, score INTEGER NOT NULL)") # Création de la base de données
baseDeDonnees.commit() # On envoie la requête SQL

# ajout du score et du nom dans la table joueurs
def database(score, name):
    best = []
    curseur.execute("INSERT INTO joueurs (name, score) VALUES (? , ?)", (name ,score)) # On ajoute un enregistrement
    baseDeDonnees.commit()
    curseur.execute("SELECT name,score FROM joueurs ORDER BY SCORE DESC")#on récupère les noms et scores de la table joueurs classé par score décroissant
    for contact in curseur.fetchall():
        best.append(contact[0])
        best.append(contact[1])# on y rajoute dans une liste que l'on retourne 
    return best

#on récupère le nom écrit par le joueur pour l'insérer dans la bdd
def enterName(font, text):
        #curseur.execute("DELETE FROM joueurs WHERE id > 0") (permet de supprimer les élément d'une bdd ou l'id est sup à 0)
        #baseDeDonnees.commit()
        #création de l'image
        bg1_image = pygame.image.load("img/ecran_mort.png").convert()
        #remeusure de la surface de l'image
        back = pygame.transform.scale(bg1_image, (SCREEN_WIDTH, SCREEN_HEIGHT) )
        #affichage du fond
        screen.blit(back, (0,0))
        name = font.render( text, True, 'yellow')
        #création de la zone d'écriture
        rect = name.get_rect()
        rect.topleft = ((SCREEN_WIDTH/5, SCREEN_HEIGHT/1.5))
        # création du curseur d'écriture, la barre qui clignote
        cursor = Rect(rect.topright, (3, rect.height))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit
            
            if event.type == KEYDOWN:
                #permet d'effacer le dernier caractere si on appuie sur effacer
                if event.key == K_BACKSPACE:
                    if len(text)>0:
                        text =  text[:-1]
                else:
                    # rajoute à text le caractère sur lequel on vient de cliquer
                    text += event.unicode
                #affiche le texte
                img = font.render(text, True, 'yellow')
                rect.size=img.get_size()
                cursor.topleft = rect.topright
        screen.blit(name, rect)
        #permet le clignotement de la barre
        if time.time() % 1 > 0.5:
            pygame.draw.rect(screen, "yellow", cursor)
        pygame.display.update()

        return text
   