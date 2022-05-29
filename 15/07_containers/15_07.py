def inp():
    while True:
        try:
            container = int(input('Введите вес контейнера: '))
            if container < 0 or container > 200 or type(container) == float:
                raise Exception
            break
        except Exception:
            print('Вес контейнера может быть от 0 до 200 кг, целое число')
    return container
sum = int(input('Кол-во контейнеров: '))
containers = []
for i in range(sum):
    containers.append(inp())
print('Новый контейнер: ', end='')
new_container = inp()
position = 0
for i in range(len(containers)):
    if new_container > containers[i]:
        position = i + 1
        break
print('Номер, куда встанет контейнер:', position)

