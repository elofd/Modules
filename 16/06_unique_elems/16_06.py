numbers1 = []
numbers2 = []
for i in range(1, 4):
    print('Введите', i, '-е число для первого списка: ', end='')
    number = int(input())
    numbers1.append(number)
for i in range(1, 8):
    print('Введите', i, '-е число для второго списка: ', end='')
    number = int(input())
    numbers2.append(number)
print('Первый список:', numbers1)
print('Второй список:', numbers2)
numbers1.extend(numbers2)
for i in numbers1:
    for j in range(numbers1.count(i) - 1):
        numbers1.remove(i)
print(numbers1)
