def add_number():
    name = input('Введите имя и фамилию нового контакта (через пробел): ').split()
    if tuple(name) in contacts.keys():
        print('Такой человек уже есть в контактах.')
    else:
        number = int(input('Введите номер телефона: '))
        contacts[tuple(name)] = number
    print('Текущий словарь контактов:', contacts)

def seach():
    family = input('Введите фамилию для поиска: ').title()
    for key, value in contacts.items():
        if family in key:
            print(key[0], key[1], ':', value)
            break
    else:
        print('Такого человека нет в списке контактов')

contacts = {}
while True:
    print('Введите номер действия: '
          '\n1. Добавить контакт '
          '\n2. Найти человека ')
    action = int(input())
    if action == 1:
        add_number()
    elif action == 2:
        seach()
    elif action == 0:
        break
