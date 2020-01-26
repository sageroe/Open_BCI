# -*- coding: utf-8 -*-

import multiprocessing as mp
import pygame as pg
import os
import pandas as pd
import filterlib as flt
import blink as blk
#from pyOpenBCI import OpenBCIGanglion


def blinks_detector(quit_program, blink_det, blinks_num, blink,):
    def detect_blinks(sample):
        if SYMULACJA_SYGNALU:
            smp_flted = sample
        else:
            smp = sample.channels_data[0]
            smp_flted = frt.filterIIR(smp, 0)
        #print(smp_flted)

        brt.blink_detect(smp_flted, -38000)
        if brt.new_blink:
            if brt.blinks_num == 1:
                #connected.set()
                print('CONNECTED. Speller starts detecting blinks.')
            else:
                blink_det.put(brt.blinks_num)
                blinks_num.value = brt.blinks_num
                blink.value = 1

        if quit_program.is_set():
            if not SYMULACJA_SYGNALU:
                print('Disconnect signal sent...')
                board.stop_stream()


####################################################
    SYMULACJA_SYGNALU = True
####################################################
    mac_adress = 'd2:b4:11:81:48:ad'
####################################################

    clock = pg.time.Clock()
    frt = flt.FltRealTime()
    brt = blk.BlinkRealTime()

    if SYMULACJA_SYGNALU:
        df = pd.read_csv('dane_do_symulacji/data.csv')
        for sample in df['signal']:
            if quit_program.is_set():
                break
            detect_blinks(sample)
            clock.tick(200)
        print('KONIEC SYGNAŁU')
        quit_program.set()
    else:
        board = OpenBCIGanglion(mac=mac_adress)
        board.start_stream(detect_blinks)

if __name__ == "__main__":


    blink_det = mp.Queue()
    blink = mp.Value('i', 0)
    blinks_num = mp.Value('i', 0)
    #connected = mp.Event()
    quit_program = mp.Event()

    proc_blink_det = mp.Process(
        name='proc_',
        target=blinks_detector,
        args=(quit_program, blink_det, blinks_num, blink,)
        )

    # rozpoczęcie podprocesu
    proc_blink_det.start()
    print('subprocess started')

    ############################################
    # Poniżej należy dodać rozwinięcie programu
    ############################################


pg.init() ###Przenioslem bo powinno się tutaj znajdować

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pg.image.load(canonicalized_path).convert()
                _image_library[path] = image
        return image


def main():

    screen = pg.display.set_mode((1000,640))
    ###Nazwa fontu

    font = pg.font.Font(os.path.join('other','FR.ttf'), 29)
    running = True
    clock = pg.time.Clock()

    #lista muzyki do plakatu avengersów
    _songs_avengers = ['avengers']
    pg.mixer.music.load(os.path.join('Muzyka/Avengers', 'avengers.mp3'))
    pg.mixer.music.queue(os.path.join('Muzyka/Avengers', '1.mp3'))
    pg.mixer.music.queue(os.path.join('Muzyka/Avengers', '2.mp3'))
    pg.mixer.music.queue(os.path.join('Muzyka/Avengers', '1.mp3'))
    pg.mixer.music.queue(os.path.join('Muzyka/Czas Apokalipsy', '1.mp3'))



    _currently_playing_song = None
    #ustalamy zdarzenie które ma zakończyć granie muzyki
    SONG_END = pg.USEREVENT + 1

    pg.mixer.music.set_endevent(SONG_END)
    #Ładujemy wszystkie niespędne pliki z muzyką poniżej. Za żadne skarby nie rób tego w pętli
    ###Lista wszystkich wczytanych grafik
        ### GRAFIKA REZULTATU
    fail_image = pg.image.load(os.path.join('img/Wynik', 'failed.jpg'))
        ### WSZYSTKIE PLAKATY
    avengers_plakat=pg.image.load(os.path.join('img/Plakaty', 'ave.jpg'))
    donnie_plakat=pg.image.load(os.path.join('img/Plakaty', 'don.jpg'))
    fightclub_plakat=pg.image.load(os.path.join('img/Plakaty', 'fc.jpg'))
    apocalypsenow_plakat=pg.image.load(os.path.join('img/Plakaty', 'apo.jpg'))
    scarface_plakat=pg.image.load(os.path.join('img/Plakaty', 'sc.jpg'))
        ###CAŁY INTERFEJS
    interfejs_interfejs=pg.image.load(os.path.join('img/Interfejs', 'interfejs.jpg'))
    interfejs_start=pg.image.load(os.path.join('img/Interfejs','start.jpg'))
    interfejs_tlo=pg.image.load(os.path.join('img/Interfejs','tlo.jpg'))
    plakat = avengers_plakat


    START = False
    mrugniecia=0
    musictime=5
    score = 0
    turn = 1
    while running:
        #Zdarzenia
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            #poniższy kod wykona się kiedy wciśniemy SPACE
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                     START = True
                     time_0 = pg.time.get_ticks()
            #kod poniżej wykona się kiedy dojdzie do zakończenia odtwarzania dźwięku
            screen.fill((255,255,255))
            if event.type == SONG_END:
                START = False
                print("Na na na na koniec piosenki")
                screen.blit(fail_image,(10,30))
            #wypełniamy okno kolorami i obrazkami poniżej

            if START:
                ###RUNDA PIERWSZA
                print(time_0)
                if turn == 1 :
                    text_Tytul1= font.render("Avengers", True, (255, 255, 255))
                    text2 = font.render("Runda 1/5 ", True, (255, 255, 255))
                    text3 = font.render("Punkty:"+str(score), True, (255, 255, 255))
                    text1= font.render("Ilosc mrugniec: "+str(mrugniecia), True, (255, 255, 255))
                    time_1 = pg.time.get_ticks()
                    print(time_1)
                    if time_1 - time_0 > 18000:
                        turn = 2


                if turn == 2:
                    text_Tytul1= font.render("Czas Apokalipsy", True, (255, 255, 255))
                    text2 = font.render("Runda 2/5 ", True, (255, 255, 255))
                    text3 = font.render("Punkty:"+str(score), True, (255, 255, 255))
                    text1= font.render("Ilosc mrugniec: "+str(mrugniecia), True, (255, 255, 255))
                    plakat = apocalypsenow_plakat
                    pg.display.flip()
                if blink.value == 1:
                    print('BLINK')
                    blink.value = 0
                    mrugniecia=mrugniecia+1
                    pg.display.flip()
                screen.blit(interfejs_interfejs,(0,0))
                screen.blit(text_Tytul1, (250,58)) ###Tytuł
                screen.blit(plakat,(231,145))
                screen.blit(text1, (725,92)) ###Prawy górny
                screen.blit(text2, (725,255)) ###Prawy środkowy
                screen.blit(text3, (725,410)) ### Prawy dolny
                pg.display.flip()
 ### and drugi warunek poprawna muzyka i plakat
                    ###RUNDA DRUGA
                if pg.mixer.music.get_busy() == False:
                    pg.time.wait(3000)
                    pg.mixer.music.play(1)
            pg.display.flip()
            if not START:
                    screen.blit(interfejs_start,(0,0))
                    pg.display.flip()
if __name__=="__main__":
    main()


# Zakończenie podprocesów
    proc_blink_det.join()
