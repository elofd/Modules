message = input('Сообщение: ')
new_message = ''
temp_message = ''
for i in message:
    if i.isalpha():
        temp_message += i
    else:
        new_message += temp_message[::-1]
        new_message += i
        temp_message = ''
print(new_message)