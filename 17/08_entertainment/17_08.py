import random
n = int(input('Количество палок: '))
k = int(input('Количество бросков: '))
game = ['I' for x in range(n)]
print(game)
for i in range(1, k + 1):
    b = random.randint(0, n)
    a = random.randint(0, b)
    print('Бросок', i, '.', 'Сбиты палки с номера', a, 'по номер', b)
    game[a:b + 1] = ['.' for x in range(a, b + 1)]
    print(game)
print('Результат', ''.join(map(str, game)))