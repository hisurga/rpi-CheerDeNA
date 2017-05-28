import lxml.html
import requests
from time import sleep
from datetime import datetime

def fetchGameStatus():
    DENA = "ＤｅＮＡ"
    OUT3 = "●●●"
    
    today = datetime.now()
    topUrl = "https://baseball.yahoo.co.jp/npb/schedule/?date={today:%Y%m%d}"

    # html及びroot取得
    topHtml = requests.get(topUrl).text
    topRoot = lxml.html.fromstring(topHtml)

    # 週間予定からtoday pl7で今日の試合予定パスを取り、そこからDENAの文字列を検索
    tdTeam = topRoot.xpath('//td[@class="today pl7"]/*[text()="%s"]' %DENA)

    if tdTeam == []:
        return(0, "NOGAME")

    # trの位置からscoreUrlを探したい
    tr = tdTeam[0].getparent().getparent()

    # scoreUrlの場所はtoday ctの2番目
    forScoreUrl = tr.xpath('td[@class="today ct"][2]//a/@href')

    if forScoreUrl == []:
        return(0, "NOTBEGAN")

    scoreUrl = "http://baseball.yahoo.co.jp/live/" + forScoreUrl[0] + "score";
    scoreHtml = requests.get(scoreUrl).text
    scoreRoot = lxml.html.fromstring(scoreHtml)
    
    # liveNaviの場所に{攻撃中のチーム or 試合終了}が表示されている。
    liveNavi = scoreRoot.cssselect('#livenavi p')[0].text_content()
        
    if(scoreRoot.xpath('//p[@class="o"]/b') != []):
        outCount = scoreRoot.xpath('//p[@class="o"]/b')[0].text_content()
        
    # 試合中であった場合batterspanからスライスで背番号を取得し、int型にして返す
    if (DENA in liveNavi) and not(OUT3 in outCount):
        return(1, int(scoreRoot.cssselect('#batter span')[0].text_content()[1:]))
    elif "試合終了" in liveNavi:
        return(0, "OVER")
    else:
        return(1, "OPPONENT")
    
if __name__ == "__main__":
    status, detail = fetchGameStatus()

    while True:
        if status == 0:
            if "NOGAME" in detail:
                print("今日は試合がないようです。")
                break
            elif "NOTBEGAN" in detail:
                print("今日は試合がまだのようです。")
                break
            else:
                print("試合は終了しました。")
                break
        else:
            if "OPPONENT" in detail:
                print("相手の攻撃中です。")
                sleep(15)
            else:
                print(detail + "が打席に立ってます。応援しましょう。")
                sleep(15)
    
            
