import lxml.html
import requests
from time import sleep
from datetime import datetime

DENA = "ＤｅＮＡ";

# 日付情報から某サイトのURLを取得
today = datetime.now()
topUrl = "https://baseball.yahoo.co.jp/npb/schedule/?date={today:%Y%m%d}"

# html及びroot取得
topHtml = requests.get(topUrl).text
topRoot = lxml.html.fromstring(topHtml)

# 週間予定からtoday pl7で今日の試合予定パスを取り、そこからDENAの文字列を検索
tdTeam = topRoot.xpath('//td[@class="today pl7"]/*[text()="%s"]' %DENA)

if tdTeam == []:
    print("今日は試合がないようです。")
    exit()

# trの位置からscoreUrlを探したい
tr = tdTeam[0].getparent().getparent()

# scoreUrlの場所はtoday ctの2番目
forScoreUrl = tr.xpath('td[@class="today ct"][2]//a/@href')

if forScoreUrl == []:
    print("今日は試合がまだのようです。")
    exit()

scoreUrl = "http://baseball.yahoo.co.jp/live/" + forScoreUrl[0] + "score";
scoreHtml = requests.get(scoreUrl).text
scoreRoot = lxml.html.fromstring(scoreHtml)

# liveNaviの場所に{攻撃中のチーム or 試合終了}が表示されている。
liveNavi = scoreRoot.cssselect('#livenavi p')[0].text_content()

# 試合中であった場合、batterspanから背番号取得
if DENA in liveNavi:
    print(f"{scoreRoot.cssselect('#batter span')[0].text_content()}が打席に立ってます。応援しましょう。")
elif "試合終了" in liveNavi:
    print("試合は終了しました。")
else:
    print("相手の攻撃中です。")
