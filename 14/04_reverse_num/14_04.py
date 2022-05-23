def conversely(number):
    flag = True
    whole = ''
    fraction = ''
    conv_whole = 0
    conv_fraction = 0
    for i in number:
        if i == '.':
            flag = False
        elif flag:
            whole += i
        else:
            fraction += i
    whole = int(whole)
    fraction = int(fraction)
    while whole > 0:
        conv_whole = conv_whole * 10 + whole % 10
        whole //= 10
    while fraction > 0:
        conv_fraction = conv_fraction * 10 + fraction % 10
        fraction //= 10

    return str(conv_whole) + '.' + str(conv_fraction)
x = input('Введите первое число: ')
y = input('Введите второе число: ')
print('Первое число наоборот:', conversely(x))
print('Второе число наоборот:', conversely(y))
print('Сумма:', float(conversely(x)) + float(conversely(y)))