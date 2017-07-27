#-*- coding: utf-8 -*-
import pygame.mixer

class PlayMusic:

    def __init__(self):
        pygame.mixer.init()

    def play_music(self, number):
        path = "CheerMusic/" + number + ".mp3"
        print(path)

        if not(pygame.mixer.music.get_busy()):
            try:
                pygame.mixer.music.load(path)
            except:
                pygame.mixer.music.load("CheerMusic/migi.mp3")
            pygame.mixer.music.play(1)
