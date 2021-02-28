# モンテカルロシミュレーションで円周率を求める
import random

N = 10000000   # 繰り返し回数
cnt = 0
for i in range(N):
  x = random.random() # 0～1
  y = random.random() # 0～1
  if x**2 + y**2 <= 1:
     cnt+=1
pi = 4 * cnt / N
print(pi)
