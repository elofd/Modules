n = int(input('Кол-во человек: '))
k = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', k, '-й человек')
print()
people = list(range(1, n + 1))
position = 0
while len(people) > 1:
    print('Текущий круг людей:', people)
    if position >= len(people):
        position = 0
    print('Начало счёта с номера', people[position])
    for i in range(k):
        position += 1
        if position == len(people) + 1:
            position = 1
    position -= 1
    print('Выбывает человек под номером', people[position])
    people.pop(position)
    print()
print('Остался человек под номером', people[0])