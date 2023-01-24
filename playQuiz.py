# -*- coding: utf-8 -*-
# csvファイルを読み込んでランダムな声優1人の出演歴を表示

# ライブラリをインポート
# pandas : csvファイルの情報取得
# csv : csvファイルの読み込み・書き込み
# random, math : 乱数生成
# time : カウントタイマー
import pandas as pd
import csv
import random
import math
import time

# csvファイルのパス
# デフォルトはGoogleColabでの使用が想定されている
# ローカルで動かすときは別途自身のパスを指定
path = '/content/drive/MyDrive/VoiceActQuizApp/character.csv'

# csvリスト内の声優数を取得
with open(path) as f:
    list = csv.reader(f)
    df = pd.DataFrame(list)
# csvリスト内の声優数
nActers = len(df)

# 年代とキャラクターを取得
# skiprowsは飛ばしたい行を指定、not in で見たい行を指定できる
select = math.floor(random.uniform(0, nActers))
selectActer = pd.read_csv(path, header=None, skiprows=lambda x: x not in [int(select)])

# selectActer.shape[1]を指定し列数をカウント
tmpList = []
for cnt in range(0, selectActer.shape[1]):
    tmpList.append(selectActer[cnt])

print('1. 以下に表示される出演歴から、どの声優かを当てよう！')
print('2. 一番下に入力欄が表示されるので答えを入力してね！')
print('----------------')
print('5秒後にスタートします......')
time.sleep(5)
print('-------------------------------------------')
print('～出演歴～')

# リストの各列0番目の要素を表示
# 出演歴が表示される
for index, info in enumerate(tmpList):
    if index == 0:
        answer = info[0]
    elif isinstance(info[0], str):
        print(info[0])

# 答えを入力
print('-------------------------------------------')
print('～解答～')
print('※答えが分からないときは 「no」 と入力してね！')

# 正誤判定
correctFlag = 0
inputAnswer = ''

while(correctFlag == 0):
        inputAnswer = input('フルネームで答えを入力してください: ')
        # 正解した場合
        if inputAnswer == answer:
            correctFlag = 1
            print(f'正解！答えは {answer} さんです！おみごと！')
            print('また遊んでね！')
        elif inputAnswer == 'no':
            print(f'この問題の答えは {answer} さんです！')
            print('次は正解できるように頑張ろう！')
            break
        # 不正解だった場合
        else :
            print('ざんねん、もう一度挑戦してください！')
            print('----------------')