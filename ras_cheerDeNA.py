from ras_fetchGame import fetchScoreUrl
from ras_fetchGame import fetchGameStatus
from ras_playMusic import playMusic
from ras_operateFans import initPins
from ras_operateFans import operateFans

forScoreUrl = fetchScoreUrl()

if not('/' in forScoreUrl):
    if "NOGAME" in forScoreUrl:
        print("今日は試合がないようです。")
    else:
        print("今日は試合がまだのようです。")        
    exit

else:
    playMusic("D")
    initPins()    
    while True:
        status = fetchGameStatus(forScoreUrl)
        
        if "OPPONENT" in status:
            operateFans(0)
            print("相手の攻撃中です。")
            sleep(15)
        elif "NOTBEGAN" in status:
            operateFans(0)
            print("今日は試合がまだのようです。")
            exit()
        elif "OVER" in status:
            operateFans(0)
            print("試合終了！！！！")
            exit()
        else:
            operateFans(1)
            print(status + "が打席に立ってます。応援しましょう。")
            playMusic(status)
            sleep(2)
