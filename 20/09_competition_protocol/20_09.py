n = int(input('Сколько записей вносится в протокол? '))
results = {}
for i in range(1, n + 1):
    print('{0}-ая запись:'.format(i), end=' ')
    player = input().split()
    if player[1] in results:
        if int(player[0]) > int(results[player[1]]):
            results.pop(player[1])
            results[player[1]] = int(player[0])
    else:
        results[player[1]] = int(player[0])
top_results = {}
for i in sorted(results.values(), reverse=True):
    for name in results:
        if results[name] == i:
            top_results[name] = i
            results.pop(name)
            break
print()
print('Итоги соревнований:')
count = 1
for key, value in top_results.items():
    print('{0}-е место. {1} ({2})'.format(count, key, value))
    count += 1
    if count == 4:
        break
