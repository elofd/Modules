violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
song_time = 0
for x in range(int(input('Сколько песен выбрать? '))):
    name = input('Название песни: ')
    song_time += violator_songs.get(name, 0)
print('Общее время звучания песен: {:.2f} минуты'.format(song_time))