sum = int(input('Кол-во видеокарт: '))
videocards = []
new_videocards = []
for i in range(1, sum + 1):
    print(i, 'Видеокарта: ', end='')
    videocard = int(input())
    videocards.append(videocard)
maximum = videocards[0]
for i in videocards:
    if maximum < i:
        maximum = i
for i in videocards:
    if i != maximum:
        new_videocards.append(i)
print('Старый список видеокарт:', ' '.join(map(str, videocards)))
print('Новый список видеокарт', ' '.join(map(str, new_videocards)))
