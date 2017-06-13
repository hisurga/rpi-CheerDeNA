#-*- coding: utf-8 -*-
from ras_fetchGame import fetchScoreUrl
from ras_fetchGame import fetchGameStatus
from ras_playMusic import playMusic
from ras_operateFans import initPin
from ras_operateFans import operateFan
from time import sleep

forScoreUrl = fetchScoreUrl()

if not('/' in forScoreUrl):
    if "NOGAME" in forScoreUrl:
        print("今日は試合がないようです。")
    else:
        print("今日は試合がまだのようです。")        
    exit

else:
    playMusic("D")
    initPin()    
    while True:
        status = fetchGameStatus(forScoreUrl)
        
        if "OPPONENT" in status:
            operateFan(0)
            print("相手の攻撃中です。")
            sleep(15)
        elif "NOTBEGAN" in status:
            operateFan(0)
            print("今日は試合がまだのようです。")
            exit()
        elif "OVER" in status:
            operateFan(0)
            print("試合終了！！！！")
            exit()
        else:
            operateFan(1)
            print(status + "が打席に立ってます。応援しましょう。")
            playMusic(status)
            sleep(2)
