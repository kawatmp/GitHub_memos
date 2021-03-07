# モンティ・ホール問題
# （ベイズの定理における事後確率）
# 直感で正しいと思える答えと、論理的に正しい答えが異なる適例
# https://ja.wikipedia.org/wiki/%E3%83%A2%E3%83%B3%E3%83%86%E3%82%A3%E3%83%BB%E3%83%9B%E3%83%BC%E3%83%AB%E5%95%8F%E9%A1%8C
#
# 問題：3つの箱のうち、1つは当り、2つは外れが入っている。
#       回答者が1つの箱を選択した後、出題者は残りの2箱のうち外れの箱を1つ開けて
#       中を見せる。ここで回答者は、最初に選んだ箱か、残りの1箱かを選べる。
#       回答者は、選んだ箱を変更すべきか？
import random
N = 100000   # 繰り返し回数
cnt = 0        # 当り

# 最初に選んだ箱を変えない場合
for i in range(N):
  x = random.randint(1, 3)   # 当りの箱 (1 or 2 or 3)
  y = random.randint(1, 3)   # 回答者が選んだ箱
  if x == y:
    cnt+=1
print("箱を変えない場合：" + str(cnt/N))

cnt = 0
# 最初に選んだ箱を変える戦略
for i in range(N):
  x = random.randint(1, 3)   # 当りの箱 (1 or 2 or 3)
  y = random.randint(1, 3)   # 回答者が選んだ箱
  if x != y:                   # 最初に選んだ箱が外れ⇒変えるので当りになる
    cnt+=1
print("箱を変える場合：" + str(cnt/N))
