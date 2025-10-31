
#
#   stopwatch.py : StopWatch Timer written in Python 
#
#   MIT License - (c)2020-25 by @_°° Lumachina Software
#
#   Massimiliano Cosmelli (massimiliano.cosmelli@gmail.com)
#

from fonts import Fonts

import pygame, os, sys, time, datetime
from pygame.locals import *

BLACK,WHITE,RED,GREEN,BRIGHT_RED,BRIGHT_GREEN,BLUE =    (0,0,0),        \
                                                        (255,255,255),  \
                                                        (150,0,0),      \
                                                        (0,150,0),      \
                                                        (255,0,0),      \
                                                        (0,255,0),      \
                                                        (0,0,255)
GO_BUTTON_COLOR,STOP_BUTTON_COLOR = BRIGHT_GREEN,RED

X,Y = 0,1
BUTTON_RED_PRESSED, BUTTON_GREEN_PRESSED = 0,1

pygame.init()
pygame.display.set_caption('Stopwatch (c)2020-25 by @_°°  Lumachina SW ')
fps = pygame.time.Clock()   # frames/second
screen = pygame.display.set_mode((400,110))
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(BLUE)
txtfonts = Fonts(os.getcwd()+"/fonts/",(40,50))
fps_rate = 1
			
def terminate():
    # quit game
    pygame.quit()
    sys.exit()
        
def catch_event_quit(event):
    # trap events close window
    if event.type == QUIT:
        return True
    else:
        return False

def catch_event_space(event):
    # catch space key is pressed
    if event.type == KEYDOWN:
        if event.key == pygame.K_SPACE:
            return True

def catch_event_button_pressed(event):
    if event.type == pygame.MOUSEBUTTONUP:
        mouse = pygame.mouse.get_pos()
        if mouse[Y] > 60 and mouse[Y] < 110:
            if mouse[X] > 0 and mouse[X] < 200:    
                return BUTTON_GREEN_PRESSED
            elif mouse[X] > 200 and mouse[X] < 400:
                return BUTTON_RED_PRESSED
        
def update_time(actual_time):
    # update the elapsed time in hh:mm:ss format
    hh,mm,ss = actual_time
    ss = (ss + 1)%61
    if ss == 60:
        ss = ss - 60
        mm = (mm + 1)%61
        if mm == 60:
            mm = mm - 60
            hh = (hh + 1)%24
    return (hh,mm,ss)

def go_to_pause():
    print('Went on break at ' + datetime.datetime.now().strftime('%H:%M:%S'))
    attendere = True
    while attendere:
        for event in pygame.event.get():
            if catch_event_quit(event):
                terminate()
            elif catch_event_space(event) or catch_event_button_pressed(event) == BUTTON_GREEN_PRESSED:
                draw_buttons()
                pygame.display.update()
                print('Came back from break at ' + datetime.datetime.now().strftime('%H:%M:%S'))
                attendere = False
                
def draw_buttons():
    pygame.draw.rect(screen, GO_BUTTON_COLOR,(0,60,200,50))
    txtfonts.write(screen,'GO',True,(20,60))
    pygame.draw.rect(screen, STOP_BUTTON_COLOR,(200,60,200,50))
    txtfonts.write(screen,'STOP',True,(185,60))

def draw_time(actual_time):
    hh,mm,ss = actual_time
    txtfonts.write(screen,'{:02d}:{:02d}:{:02d}'.format(hh,mm,ss),True,(0,0))    

def main():
    
    t0 = time.time()

    hh,mm,ss = 0,0,0
    actual_time = (hh,mm,ss)

    print('Press SPACE BAR or use the RED and GREEN buttons to toggle timer pause')

    while True:
        
        # events management
        for event in pygame.event.get():
            if catch_event_quit(event):
                terminate()
                
            elif catch_event_space(event) or catch_event_button_pressed(event) == BUTTON_RED_PRESSED:
                draw_buttons()
                pygame.display.update()
                go_to_pause()
            
        # timer management
        if time.time()-t0 > 0.99:
            t0 = time.time()
            actual_time = update_time(actual_time)
       
        screen.blit(background,(0,0))
        
        draw_buttons()
        
        draw_time(actual_time)
        
        pygame.display.update()
        
        fps.tick(fps_rate)
        
# call main
if __name__ == '__main__':
    main()