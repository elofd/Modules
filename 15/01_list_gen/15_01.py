n = int(input('Введите число: '))
symbols = []
for i in range(1, n + 1):
    if i % 2 != 0:
        symbols.append(i)
print('Список из нечетных чисел:', symbols)


