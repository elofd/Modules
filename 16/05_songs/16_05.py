violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
playtime = 0
amount = int(input('Сколько песен выбрать? '))
for i in range(1, amount + 1):
    print('Название', i, 'песни: ', end='')
    song = input()
    for songs in violator_songs:
        for one_song in songs:
            if song == one_song:
                playtime += songs[1]
print('Общее время звучания песен:', playtime)