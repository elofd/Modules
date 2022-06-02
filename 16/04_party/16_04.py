guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    status_guest = input('Гость пришёл или ушёл? ')
    if status_guest == 'пришёл' or status_guest == 'Пришёл':
        guest = input('Имя гостя: ')
        if len(guests) < 6:
            print('Привет,', guest)
            guests.append(guest)
        else:
            print('Прости,', guest, ', но мест нет')
    elif status_guest == 'ушёл' or status_guest == 'Ушёл':
        guest = input('Имя гостя: ')
        guests.remove(guest)
    elif status_guest == 'Пора спать' or status_guest == 'пора спать':
        break
print('Вечеринка закончилась, все легли спать')
