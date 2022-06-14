n = int(input('Введите количество пар слов: '))
words = {}
for i in range(1, n + 1):
    print(i, 'пара:', end=' ')
    pair = input('').lower().split(' — ')
    words[pair[0]] = [pair[1]]
print()
while True:
    word = input('Введите слово: ').lower()
    if word in words.keys() or [word] in words.values():
        for i in words.keys():
            if i == word:
                print('Синоним:', words[i][0].title())
            elif words[i] == [word]:
                print('Синоним:', i.title())
        break
    else:
        print('Такого слова в словаре нет.')