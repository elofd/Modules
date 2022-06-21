symbols1 = 'abcd'
print('Строка:', symbols1)
symbols2 = (10, 20, 30, 40)
print('Кортеж чисел:', symbols2)
print('Результат:')
if len(symbols1) < len(symbols2):
    long = len(symbols1)
else:
    long = len(symbols2)
generator = ((symbols1[i], symbols2[i]) for i in range(long))
print(generator)
for part in generator:
    print(part)