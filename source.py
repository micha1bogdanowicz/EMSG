#!/usr/bin/python

from Tkinter import Tk
from tkFileDialog import askopenfilename
from Crypto.PublicKey import RSA
from Crypto import Random
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
window = pygame.display.set_mode((display_width,display_height)) #set display mode
graf_rect = my_grafic.get_rect(center=(display_width/2, display_height/2)) # center grafic
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

#Wypisz kazdy input w terminalu##########################
# TEST FUNCTION
def input(events):
    for event in events:
        if event.type == QUIT:
            sys.exit(0)
        else:
            print event
#########################################################
#### RSA RSA RSA RSA ####################################
# generate RSa 4096b keys, and save to file
def generate_rsa_key():
    randomgen = Random.new().read
    key = RSA.generate(4096, randomgen)
    # private key -SECRET
    private_handler = open("privateKeyFile.pem", 'w')
    private_handler.write(key.exportKey(format='PEM'))
    private_handler.close()
    # public key - use to encrypt
    public_handler = open("publicKeyFile.pem", 'w')
    public_handler.write(key.publickey().exportKey(format='PEM'))
    public_handler.close()
# encrypt RSA
def rsa_encrypter():
    public_handler = open('publicKeyFile.pem', 'r')
    Tk().withdraw()
    file_name = askopenfilename()
    file_to_encrypt = open(file_name, 'r')
    file_encrypted = open('cipher.txt', 'w')
    public_key = RSA.importKey(public_handler.read())
    msg = file_to_encrypt.read()
    cipher = public_key.encrypt(msg, 32)
    file_encrypted.write(cipher[0].encode('hex'))
    file_to_encrypt.close()
    file_encrypted.close()
    public_handler.close()
# decrypt RSA
def rsa_decrypter():
    private_handler = open('privateKeyFile.pem', 'r')
    Tk().withdraw()
    file_name = askopenfilename()
    file_to_decrypt = open(file_name, 'r')
    file_decrypted = open('plaintext.txt', 'w')
    private_key = RSA.importKey(private_handler.read())
    cipher = (file_to_decrypt.read()).decode('hex')
    msg = private_key.decrypt(cipher)
    file_decrypted.write(msg)
    file_to_decrypt.close()
    file_decrypted.close()
    private_handler.close()

#BOX dla tesktu########################################3#
def display_input(screen, message):
  "Print a message in a box in the middle of the screen"
  pygame.draw.lines(screen,(255,255,255),False, (((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 8),((screen.get_width() / 2) + 100,
                    (screen.get_height() / 2) - 8)), 1)
  if len(message) != 0:
    screen.blit(czcionka.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 30))
  pygame.display.flip()
#wprowadzenie z klawiatury##############################################
def ask(screen):
  "ask(screen) -> answer"
  pygame.font.init()
  current_string = []
  display_input(screen,"" + string.join(current_string,""))
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
    display_input(screen, "" + string.join(current_string,""))
  return string.join(current_string,"")

def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
        return event.key
    elif event.type == QUIT:
        sys.exit(0)
    else:
      pass
#############################if main *****
# welcome flag  ->   startup msg
# second flag   ->   choose nickname
if __name__ == "__main__":
    welcome=False
    second=True

    while True:
        input(pygame.event.get())
        pygame.display.flip()
        screen.fill(0)

        if welcome:
            # welcome msg
            screen.blit(my_grafic, graf_rect)
            text_rect, text_render = text_handler(text_list[0], czcionka, 0, 50)
            screen.blit(text_render, text_rect)
            pygame.display.update()
            time.sleep(1)
            text_rect, text_render = text_handler(text_list[1], czcionka, 0, 100)
            screen.blit(text_render, text_rect)
            pygame.display.update()
            time.sleep(1)
            screen.fill(0)
            welcome=False
        screen.blit(my_grafic, (10, 10))

        if second:
            # nick input
            text_rect,text_render=text_handler(text_list[2],czcionka,0,-100)
            screen.blit(text_render, text_rect)
            nick= ask(screen)
            screen.fill(0)
            screen.blit(my_grafic, (10, 10))
            nick_render = czcionka.render("Welcome "+nick, 1, (250, 250, 250))
            text_rect_nick = nick_render.get_rect(center=(((display_width / 2)), ((display_height / 2)-200)))
            second=False


        screen.blit(nick_render, text_rect_nick)
        text_rect2, text_render2 = text_handler(text_list[3], czcionka, 0, 200)
        screen.blit(text_render2, text_rect2)
        options = ask(screen)
        pygame.display.update()

        if(options=='exit'):
            sys.exit(0)

        if(options=='0'):
            text_rect, text_render = text_handler(text_list[4], czcionka, 0, -80)
            screen.fill(0)
            screen.blit(my_grafic, (10, 10))
            screen.blit(text_render, text_rect)
            pygame.display.flip()
            option_rsa=''
            text_rect, text_render = text_handler(text_list[5], czcionka, 0, -80)

            while option_rsa != "exit":
                screen.fill(0)
                screen.blit(my_grafic, (10, 10))
                screen.blit(text_render, text_rect)
                pygame.display.flip()
                option_rsa = ask(screen)

                pygame.display.update()
                if (option_rsa=="0" or option_rsa=="1"):
                    if (option_rsa == '1'):
                        generate_rsa_key()
                    text_rect, text_render = text_handler(text_list[6], czcionka, 0, -80)
                    screen.fill(0)
                    screen.blit(my_grafic, (10, 10))
                    screen.blit(text_render, text_rect)
                    pygame.display.flip()
                    time.sleep(2)
                    text_rect, text_render = text_handler(text_list[7], czcionka, 0, -80)
                    pass

                if(option_rsa=='3'):
                    rsa_encrypter()
                    text_rect, text_render = text_handler(text_list[8], czcionka, 0, -80)
                    screen.fill(0)
                    screen.blit(my_grafic, (10, 10))
                    screen.blit(text_render, text_rect)
                    time.sleep(1)
                    option_rsa='2'
                if(option_rsa=='2'):
                    text_rect, text_render = text_handler(text_list[9], czcionka, 0, -80)
                    screen.fill(0)
                    screen.blit(my_grafic, (10, 10))
                    screen.blit(text_render, text_rect)
                    pygame.display.flip()
                    time.sleep(2)
                    text_rect, text_render = text_handler(text_list[10], czcionka, 0, -80)
                if(option_rsa=='5'):
                    rsa_decrypter()
                    text_rect, text_render = text_handler(text_list[11], czcionka, 0, -80)
                    screen.fill(0)
                    screen.blit(my_grafic, (10, 10))
                    screen.blit(text_render, text_rect)
                    time.sleep(1)
                    option_rsa = '4'
                if(option_rsa=='4'):
                    option_rsa="exit"

                    pass