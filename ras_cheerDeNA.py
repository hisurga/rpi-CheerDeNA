#-*- coding: utf-8 -*-
from ras_fetchGame import fetchScoreUrl
from ras_fetchGame import fetchGameStatus
from ras_playMusic import playMusic
from time import sleep
import wiringpi2

fg = FetchGame()

status = fg.get_game_status()

if not("NOW" in status):
    print(status)
    exit()

else:
    pm = PlayMusic()

    wiringpi2.wiringPiSetupGpio()
    wiringpi2.pinMode(FANPIN, 1)

    while True:
        batter = fg.fetch_game()

        if batter is None:
            status = fg.get_game_status()
            wiringpi2.digitalWrite(FANPIN, 0)
            print(status)
            if not("OPPONENT" in status):
                exit()
            sleep(15)
            
        else:
            wiringpi2.digitalWrite(FANPIN, 1)
            print(batter + "が打席に立ってます。応援しましょう。")
            pm.play_music(status)
            sleep(2)
        