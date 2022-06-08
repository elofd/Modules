message = input('Введите строку: ')
new_message = ''
sym1 = message[0]
count = 1
for symbol in range(1, len(message)):
    if sym1 == message[symbol]:
        count += 1
    else:
        new_message += sym1
        new_message += str(count)
        count = 1
    sym1 = message[symbol]
new_message += sym1
new_message += str(count)
print('Закодированная строка:', new_message)

