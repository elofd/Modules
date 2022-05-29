word = input('Введите слово: ')
symbols = list(word)
count = 0
unique = len(symbols)
for i in symbols:
    for j in symbols:
        if i == j:
            count += 1
    if count > 1:
        unique -= 1
    count = 0
print('Кол-во уникальных букв:', unique)
