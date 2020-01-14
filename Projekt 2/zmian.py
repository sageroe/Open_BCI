# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 17:51:20 2020

@author: Sagerran and 1998krzysiek
"""

####Ważne !!! Wymiary obrazka muszą być 300x400
###Początek wymiaru plakatu 231x145
###Prawy górny 725x92
###Środkowy prawy 725x255
###Dolny prawy 725x410
### Tytuł 250x58
import pygame
import os
pygame.init() ###Przenioslem bo powinno się tutaj znajdować

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

    screen = pygame.display.set_mode((1000,640))
    ###Nazwa fontu

    font = pygame.font.Font('FR.ttf', 29)
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
    mrugniecia=0
    musictime=5
    while running:
        #Zdarzenia
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #poniższy kod wykona się kiedy wciśniemy SPACE
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                     START = True
            #kod poniżej wykona się kiedy dojdzie do zakończenia odtwarzania dźwięku
            screen.fill((255,255,255))
            if event.type == SONG_END:
                START = False
                print("Na na na na koniec piosenki")
                screen.blit(fail_image,(10,30))
            #wypełniamy okno kolorami i obrazkami poniżej

            if START:
                ###RUNDA PIERWSZA
                text_Tytul1= font.render("Avengers", True, (255, 255, 255))
                text1 = font.render("Ilość mrugnięć: " +str(mrugniecia), True, (255, 255, 255))
                text2 = font.render("Runda 1/5 ", True, (255, 255, 255))
                text3 = font.render("Pozostały czas utworu"+str(musictime)+ "sec.", True, (255, 255, 255)) ### Trzeba zimportować czas utworu
                if event.type ==pygame.KEYDOWN and event.key == pygame.K_d: ###POTENCJALNIE BD NAM LICZYŁO MRUGNIĘCIA
                    mrugniecia=mrugniecia+1
                    text1= font.render("Ilość mrugnięć: "+str(mrugniecia), True, (255, 255, 255))
                screen.blit(get_image("interfejs.jpg"),(0,0))
                screen.blit(text_Tytul1, (250,58)) ###Tytuł
                screen.blit(get_image('avenwym.jpg'),(231,145))
                screen.blit(text1, (725,92)) ###Prawy górny
                screen.blit(text2, (725,255)) ###Prawy środkowy
                screen.blit(text3, (725,410)) ### Prawy dolny
                pygame.display.flip()
 ### and drugi warunek poprawna muzyka i plakat
                    ###RUNDA DRUGA
                if pygame.mixer.music.get_busy() == False:
                    pygame.time.wait(3000)
                    pygame.mixer.music.play(1)
            pygame.display.update()
            if not START:
                    pygame.display.flip()
if __name__=="__main__":
    main()
