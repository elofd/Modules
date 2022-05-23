def danger_year(year):
    e = year
    a = year % 10
    year //= 10
    b = year % 10
    year //= 10
    c = year % 10
    d = year // 10
    if a == b == c or a == b == d or a == c == d or b == c == d:
        print(e)
year1 = int(input('Введите первый год: '))
year2 = int(input('Введите второй год: '))
print('Годы от 1900 до 2100 с тремя одинаковыми цифрами:')
for i in range(year1, year2 + 2):
    danger_year(i)