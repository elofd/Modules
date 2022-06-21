def is_prime(elem):
    flag = True
    if elem < 2:
        return False
    for x in range(2, elem // 2 + 1):
        if elem % x == 0:
            flag = False
            break
    return flag
def crypto(mes):
    return [elem for index, elem in enumerate(mes) if is_prime(index)]
print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))

