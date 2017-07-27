#-*- coding: utf-8 -*-
from ras_fetchGame import fetchScoreUrl
from ras_fetchGame import fetchGameStatus
from ras_playMusic import playMusic
from time import sleep
import wiringpi2

forScoreUrl = fetchScoreUrl()

if not('/' in forScoreUrl):
    if "NOGAME" in forScoreUrl:
        print("今日は試合がないようです。")
    else:
        print("今日は試合がまだのようです。")        
    exit

else:
    playMusic("D")

    wiringpi2.wiringPiSetupGpio()
    wiringpi2.pinMode(FANPIN, 1)

    while True:
        status = fetchGameStatus(forScoreUrl)
        
        if "OPPONENT" in status:
            wiringpi2.digitalWrite(FANPIN, 0)
            print("相手の攻撃中です。")
            sleep(15)
        elif "NOTBEGAN" in status:
            wiringpi2.digitalWrite(FANPIN, 0)
            print("今日は試合がまだのようです。")
            exit()
        elif "OVER" in status:
            wiringpi2.digitalWrite(FANPIN, 0)
            print("試合終了！！！！")
            exit()
        else:
            wiringpi2.digitalWrite(FANPIN, 1)
            print(status + "が打席に立ってます。応援しましょう。")
            playMusic(status)
            sleep(2)
