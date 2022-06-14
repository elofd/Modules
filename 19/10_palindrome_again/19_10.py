def palindrome(mes):
    pal = {}
    for sym in mes:
        if sym in pal:
            pal[sym] += 1
        else:
            pal[sym] = 1
    flag = True
    if len(mes) % 2 == 0:
        for x in pal.values():
            if x % 2 != 0:
                flag = False
                break
    else:
        count = 1
        for x in pal.values():
            if x % 2 !=0:
                count -= 1
            if count < 0:
                flag = False
                break
    if flag:
        print('Можно сделать палиндромом')
    else:
        print('Нельзя сделать палиндромом')
message = input('Введите строку: ').lower()
palindrome(message)
