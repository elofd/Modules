def sum(a):
    summa = 0
    while a > 0:
        summa += a % 10
        a = a // 10
    return summa
def numbers(b):
    num = 0
    while b > 0:
       num += 1
       b = b // 10
    return num
n = int(input('Введите число: '))
print('Сумма чисел:', sum(n))
print('Количество цифр в числе:', numbers(n))
print('Разность суммы и количества цифр:', sum(n) - numbers(n))
