def cipher(message, step):
    alphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    new_message = ''
    for symbol in message:
        if symbol in alphabet:
            new_message += alphabet[(alphabet.index(symbol) + step) % 52]
        else:
            new_message += symbol
    shift = 3
    new_message2 = ''
    for word in new_message.split(' '):
        new_word = ''
        for index in range(len(word)):
            new_word += (word[index - shift % len(word)])
        if new_word.endswith('/'):
            shift += 1
        new_message2 += new_word + ' '
    new_message3 = ''
    for symbol in new_message2:
        if symbol == '/':
            new_message3 += '\n'
        elif symbol == '(':
            new_message3 += "'"
        else:
            new_message3 += symbol
    return new_message3
mes = input('Введите сообщение: ')
move = -1

print('Зашифрованное сообщение:\n', cipher(mes, move))
