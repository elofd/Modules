n = int(input('Введите количество человек: '))
family = {}
for i in range(1, n):
    print(i, 'пара:', end=' ')
    pair = input().split()
    family[pair[0]] = pair[1]
height = {}
print(family)
print(set(family.keys()) | set(family.values()))
for man in set(family.keys()) | set(family.values()):
    count = 0
    temp_man = man
    while temp_man in family:
        temp_man = family[temp_man]
        count += 1
    height[man] = count
print('«Высота» каждого члена семьи:')
for key in sorted(height.keys()):
    print(key, height[key])
