message = input('Введите IP: ').split('.')
flag = True
while True:
    if len(message) != 4:
        print('Адрес — это четыре числа, разделённые точками.')
        break
    for x in message:
        if x.isdigit() == False:
            print(x, '— это не целое число.')
            flag = False
            break
        if int(x) < 0 or int(x) > 255:
            print(x, 'должен входить в промежуток от 0 до 255')
            flag = False
            break
    if flag:
        print('IP-адрес корректен.')
    break
