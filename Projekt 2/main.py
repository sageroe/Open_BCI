# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 17:51:20 2020

@author: Sagerran
"""

import pygame
import os

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path).convert()
                _image_library[path] = image
        return image


def main():

    pygame.init()
    screen = pygame.display.set_mode((640,480))
    running = True
    clock = pygame.time.Clock()
    #lista muzyki do plakatu avengersów
    _songs_avengers = ['avengers']
    fail_image = pygame.image.load('failed.jpg')
    _currently_playing_song = None
    #ustalamy zdarzenie które ma zakończyć granie muzyki
    SONG_END = pygame.USEREVENT + 1

    pygame.mixer.music.set_endevent(SONG_END)
    #Ładujemy wszystkie niespędne pliki z muzyką poniżej. Za żadne skarby nie rób tego w pętli
    pygame.mixer.music.load('avengers.mp3')

    START = False

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #poniższy kod wykona się kiedy wciśniemy SPACE
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                     START = True
            #kod poniżej wykona się kiedy dojdzie do zakończenia odtwarzania dźwięku
            screen.fill((255,255,255))
            if event.type == SONG_END:
                START = False
                print("Na na na na koniec piosenki")
                screen.blit(fail_image,(10,30))
            #wypełniamy okno kolorami i obrazkami poniżej

            if START:
                screen.blit(get_image('avengers.jpg'),(100,30))
                pygame.display.flip()
                if pygame.mixer.music.get_busy() == False:
                    pygame.time.wait(3000)
                    pygame.mixer.music.play(1)

            if not START:
                    pygame.display.flip()
if __name__=="__main__":
    main()
