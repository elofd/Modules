n = int(input('Введите количество заказов: '))
orders = {}
for num in range(1, n + 1):
    print(num, 'заказ:', end=' ')
    order = input('').split(' ')
    if order[0] in orders:
        if order[1] in orders[order[0]]:
            orders[order[0]][order[1]] = orders[order[0]][order[1]] + int(order[2])
        else:
            orders[order[0]][order[1]] = int(order[2])
    else:
        orders[order[0]] = {order[1]: int(order[2])}

for name in sorted(orders.keys()):
    print(name, ':')
    for item in sorted(orders[name].keys()):
        print('\t\t', item, ':', orders[name][item])