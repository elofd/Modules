films = [
    "Крепкий орешек", "Назад в будущее", "Таксист",
    "Леон", "Богемская рапсодия", "Город грехов",
    "Мементо", "Отступники", "Деревня"
]
want_films = []
love_fims = []
sum = int(input('Сколько фильмов вы хотели бы добавить? '))
for i in range(sum):
    film = input('Введите название фильма: ')
    want_films.append(film)
for i in want_films:
    if i in films:
        love_fims.append(i)
    else:
        print('Ошибка: фильма', i, 'у нас нет')
print('Ваш список любимых фильмов', ' '.join(love_fims))
