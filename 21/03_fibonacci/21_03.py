def fibonachi(n):
    cur = 1
    if n > 2:
        cur = fibonachi(n-1) + fibonachi(n-2)
    return cur

num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
print(fibonachi(num_pos))

