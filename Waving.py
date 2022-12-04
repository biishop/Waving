# Les sources du Viok
# Waving 2022(c)CHEB from Amstrad 6128 old source 1987

import pygame
from pygame.locals import *
import math
import sys
import msvcrt as m
from colour import Color as cc
import numpy as np
import matplotlib.pyplot as plt

 
def main():
    # var ecrans
    width = 1280    
    height = 720

    screen_color = (0, 0, 0)
    line_color = (255, 255, 255)
    # set le screen
    screen=pygame.display.set_mode((width,height))

    sample_rate = 1e6
    alpha = 0
    while 1==1:
        screen.fill(screen_color) # vide screen

        alpha += 1
        alpha_t = alpha * 0.0174
        # Generation son + bruit
        t = np.arange(1024*1000)/sample_rate # time vector
        f = 50e3 + 30e3 * math.cos(alpha*0.0174) # freq of tone
        
        # freq seul
        x = np.sin(2*np.pi*f*t)
        
        # freq seul + bruit
        x = np.sin(2*np.pi*f*t) + 0.2*np.random.randn(len(t))
        
        # 2 freq 
        x = np.sin(2*np.pi*f*t) +  2 * np.sin(2*np.pi*f/2*t*4) 

        # freq modul
        x = 4*np.cos(alpha_t)*np.sin(2*np.pi*(f*np.sin(alpha_t*0.2))*(2*t*np.cos(alpha_t/2))) 

        # freq modul
        x = 4*np.cos(alpha_t)*np.sin(2*np.pi*(f*np.sin(alpha_t*2))*(2*t*np.cos(alpha_t/2))) + +  2 * np.sin(2*np.pi*f/2*t*4) 

        # Graph dans le temps
        xp=0
        xvo=0
        step_x = 5
        for xv in x[0:int(width/step_x)]:
            tvx=100+xv*10
            pygame.draw.line(screen, line_color, (xp-step_x,xvo),(xp,tvx))
            xvo=tvx
            xp=xp+step_x

        # Calc fft
        tfd = np.fft.fft(x,1024)
        spectre =np.absolute(tfd)

        # Graph dans les frequences
        xp=300
        posy = 700 
        xvo=posy
        step_x = 1
        for xv in spectre[0:512]:
            tvx=posy-xv/4
            pygame.draw.line(screen, line_color, (xp,posy),(xp,tvx))
            xvo=tvx
            xp=xp+step_x
        # Affichage
        pygame.display.flip()
    m.getch()
    
# true code    
main()