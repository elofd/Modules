message = input('Введите строку: ')
message = message[message.index('h') + 1:]
message = message[::-1]
message = message[message.index('h') + 1:]


print(message)
