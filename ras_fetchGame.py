#-*- coding: utf-8 -*-
import lxml.html
import requests
from datetime import datetime
from time import sleep

class FetchGame:
    def __init__(self):
        DENA = "ＤｅＮＡ"
        OUT3 = "●●●"

        today = datetime.now()
        top_url = "https://baseball.yahoo.co.jp/npb/schedule/?date={today:%Y%m%d}"

        #取得できないとエラー発生
        top_html = requests.get(top_url).text
        top_root = lxml.html.fromstring(top_html)

        td_team = top_root.xpath('//td[@class="today pl7"]/*[text()="%s"]' %DENA)

        if td_team == []:
            self.game_status = "NOGAME"
            return

        # trの位置からscore_urlの検索
        tr = td_team[0].getparent().getparent()

        # score_urlの場所はtoday ctの2番目
        for_score_url = tr.xpath('td[@class="today ct"][2]//a/@href')

        if for_score_url == []:
            self.game_status = "NOTBEGAN"
        else:
            self.game_status = "NOW"
            self.game_url = for_score_url[0]

    def fetch_game(self):
        score_url = "http://baseball.yahoo.co.jp/live/" + self.game_url + "score"

        #取得できないとエラー発生
        score_html = requests.get(score_url).text
        score_root = lxml.html.fromstring(score_html)
        
        live_navi = score_root.cssselect('#liveNavi p')[0].text_content()

        if(score_root.xpath('//p[@class="o"]/b') != []):
            out_count = score_root.xpath('//p[@class="o"]/b')[0].text_content()
        else:
            self.game_status = "NOTBEGAN"
            return None
                    
        if (DENA in live_navi) and not(OUT3 in out_count):
            return(score_root.cssselect('#batter span')[0].text_content()[1:])
        elif "試合終了" in live_navi:
            self.game_status = "NOGAME"
            return None
        elif "試合前" in live_navi:
            self.game_status = "NOTBEGAN"
            return None
        else:
            self.game_status = "OPPONENT"
            return None

    def get_game_status(self):
        return self.game_status
    
if __name__ == "__main__":
    fg = FetchGame()

    status = fg.get_game_status()

    if not("NOW" in status):
        print(status)
        exit()
    else:
        while True:
            batter = fg.fetch_game()

            if batter is None:
                print(fg.get_game_status())
            else:
                print(batter + "が打席に立ってます。応援しましょう。")
            sleep(10)
