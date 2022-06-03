import random
team1 = [round(random.uniform(5, 10), 2) for x in range(20)]
team2 = [round(random.uniform(5, 10), 2) for x in range(20)]
team3 = [(team1[x] if team1[x] > team2[x] else team2[x]) for x in range(20)]
print('Первая команда:', team1)
print('Вторая команда:', team2)
print('Победители тура:', team3)