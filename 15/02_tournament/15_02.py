players = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
first_day = []
index = len(players)
for i in range(index):
    if i % 2 == 0:
        first_day.append(players[i])
print(first_day)