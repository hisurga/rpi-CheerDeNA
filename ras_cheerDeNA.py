import pygame.mixer
import time
from ras_baseballWEB import fetchScoreUrl
from ras_baseballWEB import fetchGameStatus

def playMusic(number):
    if "D" in number:
        pygame.mixer.init()
        return
    path = "CheerMusic/" + number + ".mp3"
    print(path)
    if not(pygame.mixer.music.get_busy()):
        try:
            pygame.mixer.music.load(path)
        except:
            pygame.mixer.music.load("CheerMusic/migi.mp3")
        pygame.mixer.music.play(1)
            

if __name__ == "__main__":
    forScoreUrl = fetchScoreUrl()
    if not('/' in forScoreUrl):
        if "NOGAME" in forScoreUrl:
            print("今日は試合がないようです。")
        else:
            print("今日は試合がまだのようです。")        
        exit
    else:
        playMusic("D")
        while True:
            status = fetchGameStatus(forScoreUrl)

            playMusic("51")
            
            '''
            if "OPPONENT" in status:
                print("相手の攻撃中です。")
                sleep(15)
            elif "NOTBEGAN" in status:
                print("今日は試合がまだのようです。")
                exit()
            elif "OVER" in status:
                print("試合終了！！！！")
                exit()
            else:
                print(status + "が打席に立ってます。応援しましょう。")
                playMusic(status)
                sleep(2)
            '''

                
