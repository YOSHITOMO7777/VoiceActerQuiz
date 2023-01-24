# -*- coding: utf-8 -*-

# ライブラリをインポート
# requests : URLを開くために使用
# BeautifulSoup(bs4) : HTMLからデータ抽出
# csv : csvファイルの読み込み・書き込み
import requests
from bs4 import BeautifulSoup
import csv

# wikipediaのURLを指定
url = input('クイズリストに追加したい声優のwikipediaのURLを入力してください: ')

# ページリクエストを送信
res = requests.get(url)

# HTMLを取得
soup = BeautifulSoup(res.text, 'html.parser')

# 取得したい要素のid,class,タグ名を指定して情報を取得
# 声優名を取得
name = soup.select('.mw-page-title-main')
# キャラクター歴を取得
characters = soup.find('dl')

# 取得したテキストをリストに変換する
charaList = [name[0].contents[0]]
for id, line in enumerate(characters):
    text = line.getText()
    print(f'{id} : {text}')
    charaList.append(f'{text}')

# csvファイルのパス
# デフォルトはGoogleColabでの使用が想定されている
# ローカルで動かすときは別途自身のパスを指定
path = '/content/drive/MyDrive/VoiceActQuizApp/character.csv'

# csvファイルの書き込み
# 書き込みモード (w:上書き, a:追記)
with open(path, 'a', encoding='utf_8_sig') as f:
    writer = csv.writer(f)
    writer.writerow(charaList)

print(f'追加した声優: {name[0].contents[0]}')
