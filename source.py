#!/usr/bin/python

import pygame, sys, os,time,string
from pygame.locals import *
from texts import list as text_list

# Settings ##################################################
pygame.init()
display_width=800
display_height=600
czcionka = pygame.font.SysFont("georgia", 20) #font
my_grafic = pygame.image.load('background001.jpg') #main grafic
pygame.display.set_caption("EncrypterMSG") #Window name
window = pygame.display.set_mode((display_width,display_height))
graf_rect = my_grafic.get_rect(center=(display_width/2, display_height/2))
#pobranie informacji o ekranie
screen = pygame.display.get_surface()


##########################################################
#Function: text_handler
# get_rect in 3 line get a argv 'center='
# x,y use to modification this formule:
# ((display_width/2)+x),((display_height/2)+y)
# choose all '0' if you want center obj.
# return tuple (text_rect,text_render)
def text_handler(text,font,x,y):
    text_render=font.render(text,1,(250,250,250))
    text_rect=text_render.get_rect(center=(((display_width/2)+x),((display_height/2)+y)))
    return (text_rect,text_render)
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
#############################if main *****
# welcome flag  ->   startup msg
# second flag   ->   choose nickname
welcome=True
second=True



while True:
    input(pygame.event.get())
    pygame.display.flip()

    if welcome:
        screen.blit(my_grafic, graf_rect)
        text_rect, text_render = text_handler(text_list[0], czcionka, 0, 50)
        screen.blit(text_render, text_rect)
        pygame.display.update()
        time.sleep(2)
        text_rect, text_render = text_handler(text_list[1], czcionka, 0, 100)
        screen.blit(text_render, text_rect)
        pygame.display.update()
        time.sleep(2)
        screen.fill(0)
        welcome=False
    screen.blit(my_grafic, (10, 10))
    if second:
        text_rect,text_render=text_handler(text_list[2],czcionka,0,-100)
        screen.blit(text_render, text_rect)
        nick= ask(screen,"")
        screen.fill(0)
        screen.blit(my_grafic, (10, 10))
        nick_render = czcionka.render("Welcome "+nick, 1, (250, 250, 250))
        text_rect = text_render.get_rect(center=(((display_width / 2)), ((display_height / 2))))
        second=False
    screen.blit(nick_render, text_rect)
    text_rect2, text_render2 = text_handler(text_list[3], czcionka, 0, 200)
    screen.blit(text_render2, text_rect2)