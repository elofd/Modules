n = int(input('Кол-во друзей: '))
friends = []
for i in range(n):
    friends.append(0)
k = int(input('Долговых расписок: '))
for i in range(k):
    to = int(input('Кому? ')) - 1
    fr = int(input('От кого? ')) - 1
    credit = int(input('Сколько? '))
    friends[to] += credit
    friends[fr] -= credit
print('Баланс друзей:')
for i in range(len(friends)):
    print(i + 1, ':', friends[i])