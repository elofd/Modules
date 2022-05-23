def circle(a, b, radius):
    if abs(x) <= r and abs(y) <=r:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')
print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
r = int(input('Введите радиус: '))
circle(x, y, r)