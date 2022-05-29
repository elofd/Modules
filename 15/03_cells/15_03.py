n = int(input('Кол-во клеток: '))
cells = []
for i in range(1, n + 1):
    print('Эффективность', i, 'клетки: ', end='')
    eff = int(input())
    if eff < i:
        cells.append(eff)
print('Неподходящие значения:', ' '.join(map(str, cells)))
