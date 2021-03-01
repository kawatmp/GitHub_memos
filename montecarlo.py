# モンテカルロシミュレーション
import random
import math

# 円周率を求める
N = 1000000   # 繰り返し回数
cnt = 0
for i in range(N):
  x = random.random() # 0～1
  y = random.random() # 0～1
  if x**2 + y**2 <= 1:
     cnt+=1
pi = 4 * cnt / N
print(pi)

# シュタイナー木問題（線分が最小になる点を求める）

# 正方形の対角を結んだ場合(4つの線分)
distance = 2 * math.sqrt(2)
print(distance)
# 5つの線分の場合
m1 = n1 = m2 = n2 = 0
for i in range(N):
  x1 = random.random()
  y1 = random.random()
  x2 = random.random()
  y2 = random.random()
  d_total = math.sqrt((x1-0)**2+(1-y1)**2) + math.sqrt((1-x1)**2+(1-y1)**2) + math.sqrt((x2)**2+(y2)**2) + math.sqrt((1-x2)**2+(y2)**2) + math.sqrt((x1-x2)**2+(y1-y2)**2)
  if d_total < distance:
    distance = d_total
    m1 = x1
    n1 = y1
    m2 = x2
    n2 = y2
print("min distance is " + str(distance))
print("pos1 : " + str(m1) + " , " + str(n1))
print("pos2 : " + str(m2) + " , " + str(n2))
