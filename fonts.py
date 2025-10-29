
# fonts.py : load the arcade game fonts

import pygame, os, sys, time
from pygame.locals import *

class Fonts():

    def __init__(self,fonts_path,dim):
        # load the character fonts
        self.char_dimension = dim
        self.distance_between_chars = dim[0]
        self.fonts_path = fonts_path   # arcade-style black & white characters fonts
        if not os.path.exists(self.fonts_path):
            print("Path error, fonts directory doesn't exists!")
            pygame.quit()
            sys.exit()
        self.indices = [0,
                        33,34,35,36,37,38,39,40,41,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,
                        63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]
        self.chars,self.chars_inv = [None]*128,[None]*128
        for i in self.indices:
            self.chars[i] = pygame.image.load(os.path.join(self.fonts_path,'black/CHAR_'+str(i)+'.png'))
            self.chars[i] = pygame.transform.scale(self.chars[i], self.char_dimension)
            self.chars_inv[i] = pygame.image.load(os.path.join(self.fonts_path,'white/CHAR_'+str(i)+'.png'))
            self.chars_inv[i] = pygame.transform.scale(self.chars_inv[i], self.char_dimension)
            
            
    def get_char(self,char,mode_white):
        # get ascii number of a char
        try:
            if not mode_white:
                return self.chars[ord(char)]
            else:
                return self.chars_inv[ord(char)]
        except IndexError:
            print(f'ERROR INDEXING CHAR WITH ASCII CODE: {ord(char)}')
            
    def put_char(self,screen,char,mode_white,pos):
        # write to screen char as image
        char_surface = self.get_char(char,mode_white)
        if char_surface != None:
            screen.blit(char_surface,pos)
            
    def write(self,screen,word,mode_white,pos):
        # write to screen a string made by chars images
        for char in word:
            pos = (pos[0]+self.distance_between_chars,pos[1])
            self.put_char(screen,char.upper(),mode_white,pos)
            