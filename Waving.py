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

        alpha += 2

        # Generation son + bruit
        t = np.arange(1024*1000)/sample_rate # time vector
        f = 50e3 + 30e3 * math.cos(alpha*0.0174) # freq of tone
        x = np.sin(2*np.pi*f*t) + 0.2*np.random.randn(len(t))

        # Graph dans le temps
        xp=0
        xvo=0
        step_x = 5
        for xv in x[0:int(width/step_x)]:
            tvx=100+xv*10
            pygame.draw.line(screen, line_color, (xp-step_x,xvo),(xp,tvx))
            xvo=tvx
            xp=xp+step_x

        # Calc spectre
        fft_size = 1024
        num_rows = int(np.floor(len(x)/fft_size))
        spectrogram = np.zeros((num_rows, fft_size))
        spectrogramm = np.zeros(fft_size)
        for i in range(num_rows):
            spectrogram[i,:] = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(x[i*fft_size:(i+1)*fft_size])))**2)
        spectrogram = spectrogram[:,fft_size//2:]

        # Graph dans les frequences
        xp=0
        xvo=0
        step_x = 1
        for xv in spectrogram[512,:]:
            tvx=300+xv
            pygame.draw.line(screen, line_color, (xp-step_x,xvo),(xp,tvx))
            xvo=tvx
            xp=xp+step_x
        # Affichage
        pygame.display.flip()
    m.getch()
    
# true code    
main()