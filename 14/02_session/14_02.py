print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))
if x1 != x2:
    x_diff = x1 - x2
    y_diff = y1 - y2
    k = y_diff / x_diff
    b = y2 - k * x2
elif y1 != y2:
    x_diff = x1 - x2
    y_diff = y1 - y2
    k = x_diff / y_diff
    b = x2 - k * y2
print("Уравнение прямой, проходящей через эти точки:")
print("y = ", k, " * x + ", b)