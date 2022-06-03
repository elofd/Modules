def analyzer(mes):
    vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
    mes = [x for x in mes if x in vowels]
    return mes
message = list(input('Введите текст: ').lower())
print('Список гласных букв:', analyzer(message))
print('Длина списка:', len(analyzer(message)))