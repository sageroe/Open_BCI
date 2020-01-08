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
    _songs_1 = ['avengers']

    SONG_END = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(SONG_END)
    pygame.mixer.music.load('avengers.mp3')
    pygame.mixer.music.play()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == SONG_END:
                print("songs end has come")
        screen.fill((255,255,255))
        screen.blit(get_image('avengers.jpg'),(100,30))
        pygame.display.flip()
if __name__=="__main__":
    main()
