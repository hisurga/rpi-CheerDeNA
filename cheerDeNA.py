import pygame.mixer
import time

'''
# mixerモジュールの初期化
pygame.mixer.init()
# 音楽ファイルの読み込み
pygame.mixer.music.load("ファイル名.mp3")
# 音楽再生、および再生回数の設定(-1はループ再生)
pygame.mixer.music.play(-1)

time.sleep(60)
# 再生の終了
pygame.mixer.music.stop()
'''

if __name__ == "__main__":
    forScoreUrl = fetchScoreUrl()
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
                    print(detail + "が打席に立ってます。応援しましょう。")
                    sleep(15)
