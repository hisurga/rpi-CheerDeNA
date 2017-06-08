from ras_fetchGame import fetchScoreUrl
from ras_fetchGame import fetchGameStatus
from ras_playMusic import playMusic
#import wiringpi

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
