import pygame, sys, os,time
from pygame.locals import *

pygame.init()

#Utworzenie okienka | etykieta | grafika#####################
display_width=800
display_height=600
window = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("EncrypterMSG")
#grafika tla
my_grafic = pygame.image.load('background001.jpg')
graf_rect = my_grafic.get_rect(center=(display_width/2, display_height/2))
#pobranie informacji o ekranie
screen = pygame.display.get_surface()
##############################################################

#Pole tekstowe - WELCOME##########################################
czcionka = pygame.font.SysFont("georgia", 20)
welcome_text="Pr3daTOR presents..."
welcome_text2="EncrypterMSG"
text_rendeer=czcionka.render(welcome_text,1,(250,250,250))
text_rendeer2=czcionka.render(welcome_text2,1,(250,250,250))
text_rect = text_rendeer.get_rect(center=(display_width/2, display_height/2+50))
text_rect2 = text_rendeer2.get_rect(center=(display_width/2, display_height/2+100))
##################################################################

#Wypisz kazdy input w terminalu##########################
def input(events):
    for event in events:
        if event.type == QUIT:
            sys.exit(0)
        else:
            print event
#########################################################

welcome=True
while True:
    input(pygame.event.get())
    pygame.display.flip()

    if welcome:
        screen.blit(my_grafic, graf_rect)
        screen.blit(text_rendeer, text_rect)
        pygame.display.update()
        time.sleep(2)
        screen.blit(text_rendeer2, text_rect2)
        pygame.display.update()
        time.sleep(2)
        screen.fill(0)
        welcome=False

    screen.blit(my_grafic, (10,10))

