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
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image
def main():
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    running = True
    clock = pygame.time.Clock()
    #lista muzyki do plakatu avengersów
    _songs_avengers = ['avengers']

    _currently_playing_song = None
    #ustalamy zdarzenie które ma zakończyć granie muzyki
    SONG_END = pygame.USEREVENT + 1

    pygame.mixer.music.set_endevent(SONG_END)
    pygame.mixer.music.load('avengers.mp3')

    START = False

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #poniższy kod wykona się kiedy wciśniemy SPACE
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                     pygame.mixer.music.play()
                     START = True
            #kod poniżej wykona się kiedy dojdzie do zakończenia odtwarzania dźwięku
            if event.type == SONG_END:
                print("songs end has come")
            #wypełniamy okno kolorami i obrazkami poniżej                
            screen.fill((255,255,255))
            if START:
                screen.blit(get_image('avengers.jpg'),(100,30))

        pygame.display.flip()
if __name__=="__main__":
    main()
