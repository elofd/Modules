def original_mes(mes):
    original = {}
    for i in message:
        if i in original:
            original[i] += 1
        else:
            original[i] = 1
    print('Оригинальный словарь частот:')
    for i in sorted(original.keys()):
        print('{0} : {1}'.format(i, original[i]))
    inversion = {}
    for i in original.keys():
        if original[i] not in inversion.keys():
            inversion[original[i]] = []
        add = inversion[original[i]]
        add.append(i)
        inversion[original[i]] = add
    print('Инвертированный словарь частот:')
    for i in sorted(inversion.keys()):
        print('{0} : {1}'.format(i, inversion[i]))

message = input('Введите текст: ').lower()
original_mes(message)


