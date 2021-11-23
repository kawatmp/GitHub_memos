# coding: Shift_JIS
import random
import time
import os

# ライフゲーム（ルールは以下）
#   過密：周囲に1が4つ以上ある時
#   過疎：周囲に1が1つ以下ある時
#   誕生：周囲に1が3つある時
#   生存：周囲に1が2つか3つある時
sedai = 100  # 世代数
s = 10       # ステージの一辺の長さ
rate = 70    # 初期値で、生物を入れる比率(％)
stage1 = [[0 for i in range(s)] for j in range(s)]  # 現世代用
stage2 = [[0 for i in range(s)] for j in range(s)]  # 次世代用

# 結果表示用の関数
def print_stage(x, ar):
  os.system('cls')
  print(str(x+1) + "世代目")
  for x in range(s):
    print(ar[x])
  time.sleep(1)
  return

# 計算処理を行う
def calc(sedai, s, stage1, stage2):
  for x in range(sedai):
    for i in range(s):     # 0～s-1の範囲
      for j in range(s):
        cnt = 0
        # stage1[i][j]の周囲8個を調べる
        if (i!=0) and (j!=0) and (stage1[i-1][j-1] == 1):
          cnt += 1
        if (i!=0) and (stage1[i-1][j] == 1):
          cnt += 1
        if (i!=0) and (j!=s-1) and (stage1[i-1][j+1] == 1):
          cnt += 1
        if (j!=0) and (stage1[i][j-1] == 1):
          cnt += 1
        if (j!=s-1) and (stage1[i][j+1] == 1):
          cnt += 1
        if (i!=s-1) and (j!=0) and (stage1[i+1][j-1] == 1):
          cnt += 1
        if (i!=s-1) and (stage1[i+1][j] == 1):
          cnt += 1
        if (i!=s-1) and (j!=s-1) and (stage1[i+1][j+1] == 1):
          cnt += 1
        # 次世代に入れる
        stage2[i][j] = stage1[i][j]
        if cnt >= 4:      # 過密
          stage2[i][j] = 0
        elif cnt <= 1:   # 過疎
          stage2[i][j] = 0
        elif cnt==3:     # 誕生
          stage2[i][j] = 1
    stage1 = stage2
    print_stage(x, stage1)
  return

# main処理
for i in range(s):
  for j in range(s):
    if (random.randint(1, 100)<=rate):
      stage1[i][j] = 1  # 乱数でstage1に初期値を入れる
calc(sedai, s, stage1, stage2)    # ここから世代毎の処理
