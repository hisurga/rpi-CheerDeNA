import lxml.html
import requests
from time import sleep
from datetime import datetime

DENA = "ＤｅＮＡ";

def cheerPlayer(uniformNo):
    print(uniformNo + "が打席に立ってます。応援しましょう。")
    time.sleep(15)

if __name__ == "__main__":
    today = datetime.now()
    topUrl = "https://baseball.yahoo.co.jp/npb/schedule/?date={today:%Y%m%d}"
    #topUrl = "https://baseball.yahoo.co.jp/npb/schedule/?date=20170525"

    topHtml = requests.get(topUrl).text
    topRoot = lxml.html.fromstring(topHtml)
    
    #listTeam = topRoot.xpath('//td[@class="today pl7"]/a')
    #linkScore = topRoot.xpath('//td[@class="today ct"]/a/@href')

    listTeam = topRoot.xpath('//td[@class="today pl7"]/*[text()="%s"]' %DENA)
    team = listTeam[0].getparent().getparent()


#    print(lxml.html.tostring(listTeam[0]))
#    print(listTeam[0].text_content())
    
    if listTeam == []:
        print("今日は試合が{ないorまだ}のようです。")
        exit()

    gameUrl = "http://baseball.yahoo.co.jp/live/" + team.xpath('td[@class="today ct"][2]//a/@href')[0] + "score";
        
    '''
    for num in range(len(listTeam)):
        if listTeam.pop(0).text_content() == DENA:
            gameUrl = "http://baseball.yahoo.co.jp/live/" + linkScore[num // 2] + "score";
            break

    if gameUrl == "":
        print("今日は試合が{まだのor終了した}ようです。")
        exit()

    '''

    gameHtml = requests.get(gameUrl).text
    gameRoot = lxml.html.fromstring(gameHtml)

    if DENA in gameRoot.cssselect('#livenavi p')[0].text_content():
        print(f"{gameRoot.cssselect('#batter span')[0].text_content()}が打席に立ってます。応援しましょう。")

#        ●●●
'''
    while True:
        gameHtml = requests.get(gameUrl).text
        root = lxml.html.fromstring(gameHtml)
        var =root.xpath('//p[@class="s"]/b')

        print (var)

#        ●●●
        while DENA in root.cssselect('#livenavi p')[0].text_content():
            cheerPlayer(root.cssselect('#batter span')[0].text_content())
            root = lxml.html.fromstring(requests.get(gameurl).text)
        time.sleep(15)
'''
