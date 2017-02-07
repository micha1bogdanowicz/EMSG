import pygame, sys, os,time,string
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

#Wiecej tekstu###########################################
text=["Input your nickname: "]
text_render3=czcionka.render(text[0],1,(250,250,250))
text_rect3 = text_render3.get_rect(center=(display_width/2, display_height/2-100))


#########################################################

#Wypisz kazdy input w terminalu##########################
def input(events):
    for event in events:
        if event.type == QUIT:
            sys.exit(0)
        else:
            print event
#########################################################

#BOX dla tesktu########################################3#
def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()
##########################################################
def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  display_box(screen, question + " " + string.join(current_string,""))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, question + " " + string.join(current_string,""))
  return string.join(current_string,"")

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

welcome=True
second=True
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
    screen.blit(my_grafic, (10, 10))
    if second:
        screen.blit(text_render3, text_rect3)
        nick= ask(screen,"")
        screen.fill(0)
        screen.blit(my_grafic, (10, 10))
        nick = czcionka.render("Welcome "+nick, 1, (250, 250, 250))
        second=False
    screen.blit(nick, text_rect3)
