# 巡回セールスマン問題(TSP)を、Pythonの遺伝的アルゴリズム(GA)で解くプログラム
import numpy as np
import random
import matplotlib.pyplot as plt

# http://samuiui.com/2019/10/27/python%E3%81%A7%E9%81%BA%E4%BC%9D%E7%9A%84%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0%EF%BC%88ga%EF%BC%89%E3%82%92%E5%AE%9F%E8%A3%85%E3%81%97%E3%81%A6%E5%B7%A1%E5%9B%9E%E3%82%BB%E3%83%BC/
# https://colab.research.google.com/drive/1Hf5zS8nA6OyU_VGRrKyVNWxn7lRzl7iy#scrollTo=CkMjx8gh2Nvm

print("start")

# まず巡回する都市を乱数で作る
def generate_rand_cities(num_cities):
    positions = np.zeros((num_cities, 2))
    for i in range(num_cities):
        positions[i, 0] = random.random()
        positions[i, 1] = random.random()
    return positions

# 初期個体を生成する
def generate_init_genes(num_indivisual, num_cities):
    genes = np.zeros((num_indivisual, num_cities), dtype=np.int16)
    for i in range(num_indivisual):
        genes[i,] = random.sample(range(num_cities), k=num_cities)
    return genes

# 一個体の経路の長さを求める
def sum_path(cities, gene):
    sum = 0.
    for i in range(len(cities)-1):
        sum += np.linalg.norm(cities[int(gene[i])]-cities[int(gene[i+1])])
    return sum

# 一世代分の個体のそれぞれの経路長を求める
def genes_path(genes, cities):
    pathlength_vec = np.zeros(len(genes))
    for i in range(len(genes)):
        indices = genes[i]
        pathlength_vec[i] = sum_path(cities, indices)
    return pathlength_vec

# ルーレット選択のための選択確率テーブル生成
def generate_roulette(fitness_vec):
    total = np.sum(fitness_vec)
    roulette = np.zeros(len(fitness_vec))
    for i in range(len(fitness_vec)):
        roulette[i] = fitness_vec[i]/total
    return roulette

# ルーレット選択
def roulette_choice(fitness_vec):
    roulette = generate_roulette(fitness_vec)
    choiced = np.random.choice(len(roulette), 2, replace=True, p=roulette)
    return choiced

#部分的交叉
def partial_crossover(parent1, parent2):
    num = len(parent1)
    cross_point = random.randrange(0, num-1)
    child1 = parent1
    child2 = parent2
    for i in range(num - cross_point):
        target_index = cross_point + i
        
        target_value1 = parent1[target_index]
        target_value2 = parent2[target_index]
        exchange_index1 = np.where(parent1 == target_value2)
        exchange_index2 = np.where(parent2 == target_value1)

        child1[target_index] = target_value2
        child2[target_index] = target_value1
        child1[exchange_index1] = target_value1
        child2[exchange_index2] = target_value2
    return child1, child2

# 突然変異（転座）  ランダムで選んだ２要素を交換する
def translocation_mutation(genes, num_mutation, p_value):
    mutated_genes = genes
    for i in range(num_mutation):
        mutation_flg = np.random.choice(2, 1, p = [1-p_value, p_value])
        if mutation_flg == 1:
            mutation_value = np.random.choice(genes[i], 2, replace=  False)
            mutation_position1 = np.where(genes[i] == mutation_value[0])
            mutation_position2 = np.where(genes[i] == mutation_value[1])
            mutated_genes[i][mutation_position1] = mutation_value[1]
            mutated_genes[i][mutation_position2] = mutation_value[0]
    return mutated_genes

# 都市の配置とルートの可視化
def show_cities(cities):
    for i in range(len(cities)):
        plt.scatter(cities[i][0], cities[i][1])

def show_route(cities, genes):
    for i in range(len(genes)-1):
        if i == 0:
            plt.text(cities[int(genes[i])][0], cities[int(genes[i])][1], "start")
        else:
            plt.text(cities[int(genes[i])][0], cities[int(genes[i])][1], str(i))
        plt.plot([cities[int(genes[i])][0], cities[int(genes[i+1])][0]], 
                 [cities[int(genes[i])][1], cities[int(genes[i+1])][1]])
    plt.text(cities[int(genes[i+1])][0], cities[int(genes[i+1])][1], "goal")

#################
# 実行部
num_cities = 20     # 都市数
indivisuals = 21    # 個体数
#generation = 10000 # 世代数
generation = 1000
elite = 9           # エリート選択数
p_mutation = 0.005  # 突然変異の発生確率

cities = generate_rand_cities(num_cities)
# 初期個体生成
genes = generate_init_genes(indivisuals, num_cities)
show_cities(cities)

top_indivisual=[]
max_fit = 0
for i in range(generation):  # 世代数が一定に達したら終了
    # genes_pathが評価関数(経路が短いほど良い)
    fitness_vec = np.reciprocal(genes_path(genes, cities))
    child = np.zeros(np.shape(genes))
    for j in range(int((indivisuals-elite)/2)):
        # 選択（淘汰）
        parents_indices = roulette_choice(fitness_vec)
        # 交叉（部分的交叉）
        child[2*j], child[2*j+1] = partial_crossover(genes[parents_indices[0]], 
                                                     genes[parents_indices[1]])
    
    for j in range(indivisuals-elite, indivisuals):
        child[j] = genes[np.argsort(fitness_vec)[j]]

    # 突然変異
    child = translocation_mutation(child, indivisuals-elite, p_mutation)
    top_indivisual.append(max(fitness_vec))
    genes = child
    if max(fitness_vec) > max_fit:
        max_fit = max(fitness_vec)
        show_cities(cities)
        show_route(cities, child[np.argmax(fitness_vec)])
        plt.text(0.05, 0.0, "generation: "+str(i))
        plt.show()

plt.plot(top_indivisual)
plt.xlabel("generation")
plt.ylabel("fitness")
plt.show();
