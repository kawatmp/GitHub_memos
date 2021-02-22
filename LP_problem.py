# 線形計画法の例題を、Python版のソルバ(LP modeler)で解くプログラム
# https://pypi.org/project/PuLP/
# LP problem = Linear programming problem
# 参考
# https://qiita.com/mzmttks/items/82ea3a51e4dbea8fbc17
# https://qiita.com/takobaya391076/items/49b15c1fa36734b3fa53

# 問題
# レストランで、ハンバーグとオムレツを作って売上を最大にする
# ひき肉：3800g
# たまねぎ：2100g
# ケチャップ：1200g
# ハンバーグ1個あたり、ひき肉60g、たまねぎ20g、ケチャップ20g
# オムレツ1個あたり、ひき肉40g、たまねぎ30g、ケチャップ10g
# 価格は、ハンバーグ400円/個、オムレツ300円/個
# http://www.fujilab.dnj.ynu.ac.jp/lecture/system2.pdf

from pulp import *

prob = LpProblem(name="profit", sense=LpMaximize)   # 目的関数を最大化する
#prob = LpProblem(name="profit", sense=LpMinimize)  #           最小化する

# Variables
v1 = LpVariable(name="v1", lowBound=0, cat="Integer")  # ハンバーグ
v2 = LpVariable(name="v2", lowBound=0, cat="Integer")  # オムレツ

# Objective（目的関数）
prob +=  400*v1 + 300*v2

# Constraints(制約式)
prob +=  60*v1 + 40*v2 <= 3800  # ひき肉の制約
prob +=  20*v1 + 30*v2 <= 2100  # たまねぎの制約
prob +=  20*v1 + 10*v2 <= 1200  # ケチャップの制約

# Solve the problem using the default solver
prob.solve()
print(LpStatus[prob.status])

print("Result")
print("ハンバーグ:", v1.value())
print("オムレツ:", v2.value())
