countries = {}
for x in range(1, int(input('Количество стран: ')) + 1):
    print(x, 'страна:', end=' ')
    country = input().split(' ')
    countries[country[1]] = country[0]
    countries[country[2]] = country[0]
    countries[country[3]] = country[0]
for x in range(1, 4):
    print(x, 'город:', end=' ')
    city = input('')
    if city in countries:
        print('Город {0} расположен в стране {1}'.format(city, countries[city]))
    else:
        print('По городу {0} данных нет.'.format(city))