# -*- coding: utf-8 -*-

import multiprocessing as mp
import pygame as pg
import os
import sys
import pandas as pd
import filterlib as flt
import blink as blk
from pyOpenBCI import OpenBCIGanglion


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
    SYMULACJA_SYGNALU = False
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


def main():


    ###Nazwa fontu
    screen = pg.display.set_mode((1000,640))
    icon =  pg.image.load(os.path.join('img/Interfejs', 'icon.png')).convert()
    pg.display.set_icon(icon)
    pg.display.set_caption('Soundtracker')
    font = pg.font.Font(os.path.join('other','FR.ttf'), 29)
    font2 = pg.font.Font(os.path.join('other','FR.ttf'), 45)
    running = True
    clock = pg.time.Clock()


    #lista muzyki do plakatu avengersów

    pg.mixer.music.load(os.path.join('Muzyka', 'Soundtrack.wav'))


    _currently_playing_song = None
    #ustalamy zdarzenie które ma zakończyć granie muzyki
    SONG_END = pg.USEREVENT + 1

    pg.mixer.music.set_endevent(SONG_END)
    #Ładujemy wszystkie niespędne pliki z muzyką poniżej. Za żadne skarby nie rób tego w pętli
    ###Lista wszystkich wczytanych grafik
        ### GRAFIKA REZULTATU

        ### WSZYSTKIE PLAKATY
    avengers_plakat=pg.image.load(os.path.join('img/Plakaty', 'ave.jpg')).convert()
    donnie_plakat=pg.image.load(os.path.join('img/Plakaty', 'don.jpg')).convert()
    fightclub_plakat=pg.image.load(os.path.join('img/Plakaty', 'fc.jpg')).convert()
    apocalypsenow_plakat=pg.image.load(os.path.join('img/Plakaty', 'apo.jpg')).convert()
    scarface_plakat=pg.image.load(os.path.join('img/Plakaty', 'sc.jpg')).convert()
        ###CAŁY INTERFEJS
    interfejs_interfejs=pg.image.load(os.path.join('img/Interfejs', 'interfejs.jpg')).convert()
    interfejs_start=pg.image.load(os.path.join('img/Interfejs','start.jpg')).convert()
    interfejs_tlo=pg.image.load(os.path.join('img/Interfejs','tlo.jpg')).convert()
    interfejs_koniec=pg.image.load(os.path.join('img/Interfejs','koniec.jpg')).convert()
    plakat = avengers_plakat

    mrug=[0,0,0]
    warden = [0,0,0,0,0,0]
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
                quit_program.set()
                sys.exit(0)
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False
                quit_program.set()
                sys.exit(0)
            #poniższy kod wykona się kiedy wciśniemy SPACE
            elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                     START = True
                     time_0 = pg.time.get_ticks()
            #kod poniżej wykona się kiedy dojdzie do zakończenia odtwarzania dźwięku
            screen.fill((255,255,255))
            #wypełniamy okno kolorami i obrazkami poniżej

        if START:
            ###RUNDA PIERWSZA

            if turn == 1 :
                text_Tytul1= font.render("Avengers", True, (255, 255, 255))
                text2 = font.render("Runda 1/5 ", True, (255, 255, 255))
                text3 = font.render("Punkty:"+str(score), True, (255, 255, 255))
                text1= font.render("Mrugniecia: "+str(mrugniecia), True, (255, 255, 255))
                time_1 = pg.time.get_ticks()

                if time_1 - time_0 > (3000+15900):
                    turn = 2


            if turn == 2:
                text_Tytul1= font.render("Czas Apokalipsy", True, (255, 255, 255))
                text2 = font.render("Runda 2/5 ", True, (255, 255, 255))
                text3 = font.render("Punkty:"+str(score), True, (255, 255, 255))
                text1= font.render("Mrugniecia: "+str(mrugniecia), True, (255, 255, 255))
                plakat = apocalypsenow_plakat
                time_2 = pg.time.get_ticks()
                if time_2 - time_0 > (3000+32300):
                    turn = 3
            if turn == 3:
                text_Tytul1= font.render("Fight Club", True, (255, 255, 255))
                text2 = font.render("Runda 3/5 ", True, (255, 255, 255))
                text3 = font.render("Punkty:"+str(score), True, (255, 255, 255))
                text1= font.render("Mrugniecia: "+str(mrugniecia), True, (255, 255, 255))
                plakat = fightclub_plakat
                time_3 = pg.time.get_ticks()
                if time_3 - time_0 > (3000+49400):
                    turn = 4
            if turn == 4:
                text_Tytul1= font.render("Donnie Darco", True, (255, 255, 255))
                text2 = font.render("Runda 4/5 ", True, (255, 255, 255))
                text3 = font.render("Punkty:"+str(score), True, (255, 255, 255))
                text1= font.render("Mrugniecia: "+str(mrugniecia), True, (255, 255, 255))
                plakat = donnie_plakat
                time_4 = pg.time.get_ticks()
                if time_4 - time_0 > (3000 + 64800):
                    turn = 5
            if turn == 5:
                text_Tytul1= font.render("Scarface", True, (255, 255, 255))
                text2 = font.render("Runda 5/5 ", True, (255, 255, 255))
                text3 = font.render("Punkty:"+str(score), True, (255, 255, 255))
                text1= font.render("Mrugniecia: "+str(mrugniecia), True, (255, 255, 255))
                plakat = scarface_plakat
                time_5 = pg.time.get_ticks()
                if time_5 - time_0 > (3000+81200):
                    turn=0






            if blink.value == 1:
                print('BLINK')
                blink.value = 0
                mrugniecia=mrugniecia+1

                mrug[2] = mrug[1]
                mrug[1]=mrug[0]
                mrug[0] = pg.time.get_ticks()
                if mrug[0]-mrug[2] < 3000:
                    ###Po dodaniu poniższychcd warunków gra się zawiesza w okolicy 3 tury
                    if (15900 + 3000) > mrug[2] - time_0 >(10900+3000) and warden[0] == 0:
                        score = score +1
                        warden[0] = 1
                    if (27100 + 3000) > mrug[2] - time_0 >(22100+3000) and warden[1] == 0:
                        score = score +1
                        warden[1] = 1
                    if (38000 + 3000) > mrug[2] - time_0 >(33000+3000) and warden[2] == 0:
                        score = score +1
                        warden[2] = 1
                    if (59600 + 3000) > mrug[2] - time_0 >(54600+3000) and warden[3] == 0:
                        score = score +1
                        warden[3] = 1
                    if (81200 + 3000) > mrug[2] - time_0 >(76200+3000) and warden[4] == 0:
                        score = score +1
                        warden[4] = 1

            screen.blit(interfejs_interfejs,(0,0))
            screen.blit(text_Tytul1, (250,58)) ###Tytuł
            screen.blit(plakat,(231,145))
            screen.blit(text1, (725,92)) ###Prawy górny
            screen.blit(text2, (725,255)) ###Prawy środkowy
            screen.blit(text3, (725,410)) ### Prawy dolny
            if turn == 0:
                screen.blit(interfejs_koniec,(0,0))
                wynik=font2.render(str(score), True, (255, 255, 255))
                screen.blit(wynik, (508,203))
            pg.display.flip()
 ### and drugi warunek poprawna muzyka i plakat
                    ###RUNDA DRUGA
            if pg.mixer.music.get_busy() == False and turn == 1:
                pg.time.wait(3000)
                pg.mixer.music.play(1)
        if not START and turn == 1:
                screen.blit(interfejs_start,(0,0))
                pg.display.flip()


if __name__=="__main__":
    main()


# Zakończenie podprocesów
    proc_blink_det.join()
