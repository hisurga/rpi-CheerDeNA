#-*- coding: utf-8 -*-
import lxml.html
import requests
from datetime import datetime
from time import sleep

DENA = "ＤｅＮＡ"
OUT3 = "●●●"

def fetchScoreUrl():   
    today = datetime.now()
    topUrl = "https://baseball.yahoo.co.jp/npb/schedule/?date={today:%Y%m%d}"

    topHtml = requests.get(topUrl).text
    topRoot = lxml.html.fromstring(topHtml)

    tdTeam = topRoot.xpath('//td[@class="today pl7"]/*[text()="%s"]' %DENA)

    if tdTeam == []:
        return("NOGAME")

    # trの位置からscoreUrlの検索
    tr = tdTeam[0].getparent().getparent()

    # scoreUrlの場所はtoday ctの2番目
    forScoreUrl = tr.xpath('td[@class="today ct"][2]//a/@href')

    if forScoreUrl == []:
        return("NOTBEGAN")
    else:
        return(forScoreUrl[0])

def fetchGameStatus(forScoreUrl):
    scoreUrl = "http://baseball.yahoo.co.jp/live/" + forScoreUrl + "score";
    scoreHtml = requests.get(scoreUrl).text
    scoreRoot = lxml.html.fromstring(scoreHtml)
    
    liveNavi = scoreRoot.cssselect('#livenavi p')[0].text_content()

    outCount = ""
    if(scoreRoot.xpath('//p[@class="o"]/b') != []):
        outCount = scoreRoot.xpath('//p[@class="o"]/b')[0].text_content()
        
    if (DENA in liveNavi) and not(OUT3 in outCount):
        return(scoreRoot.cssselect('#batter span')[0].text_content()[1:])
    elif "試合終了" in liveNavi:
        return("OVER")
    elif "試合前" in liveNavi:
        return("NOTBEGAN")
    else:
        return("OPPONENT")
    
if __name__ == "__main__":
    forScoreUrl = fetchScoreUrl()
    if not('/' in forScoreUrl):
        if "NOGAME" in forScoreUrl:
            print("今日は試合がないようです。")
        else:
            print("今日は試合がまだのようです。")
        exit

    else:
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
                sleep(15)
