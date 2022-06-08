message1 = input('Первая строка: ')
message2 = input('Вторая строка: ')
flag = False
if len(message2) == len(message1):
    flag = True
long = len(message1)
move = 0
new_flag = False
while flag and long > 0:
    count = 0
    for sym in range(len(message1)):
        if message2[sym] != message1[sym]:
            break
        count += 1
    if count == len(message1):
        new_flag = True
        break
    message1 += message1[0]
    message1 = message1[1:]
    move += 1
    long -= 1
if new_flag:
    print('Первая строка получается из второй со сдвигом', move)
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
