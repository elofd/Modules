message = input('Введите строку: ').split()
print(message)
count = 0
for word in message:
    temp_count = 0
    for sumbol in word:
        temp_count += 1
    if temp_count > count:
        count = temp_count
        big_word = word
print('Самое длинное слово: ', big_word)
print('Длина этого слова: ', count)