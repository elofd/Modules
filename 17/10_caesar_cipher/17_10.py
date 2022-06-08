def cipher(symbol, step):
    alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    if symbol in alphabet:
        return alphabet[(alphabet.index(symbol) + step) % 33]
    else:
        return symbol
message = input('Введите сообщение: ').lower()
move = int(input('Введите сдвиг: '))
new_message = [cipher(x, move) for x in message]
print('Зашифрованное сообщение:', ''.join(map(str, new_message)))