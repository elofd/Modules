def palindrome(mes):
    pal = {sym: mes.count(sym) for sym in mes}
    count = 0
    for value in pal.values():
        if value % 2 != 0:
            count += 1
    if count <= 1:
        print('Можно сделать палиндромом')
    else:
        print('Нельзя сделать палиндромом')
message = input('Введите строку: ').lower()
palindrome(message)
