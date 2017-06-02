import pygame.mixer
import time

def playMusic():
    pygame.mixer.init()
    pygame.mixer.music.load(".mp3")
    pygame.mixer.music.play(-1)

    #time.sleep(60)

    #pygame.mixer.music.stop()

if __name__ == "__main__":
    forScoreUrl = fetchScoreUrl()
    playMusic()
    while True:
        print("test")
        time.sleep(10)
    '''
    if not('/' in forScoreUrl):
        exit
    else:
        while True:
            status, detail = fetchGameStatus(forScoreUrl)

            if status == 0:
                if "NOGAME" in detail:
                    #print("今日は試合がないようです。")
                elif "NOTBEGAN" in detail:
                    #print("今日は試合がまだのようです。")
                else:
                    #print("試合は終了しました。")
                break
            else:
                if "OPPONENT" in detail:
                    #print("相手の攻撃中です。")
                    sleep(15)
                else:
                    #print(detail + "が打席に立ってます。応援しましょう。")
                    sleep(15)
    '''
