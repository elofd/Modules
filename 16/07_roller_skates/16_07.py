n = int(input('Кол-во коньков: '))
n_list = []
for i in range(1, n + 1):
    print('Размер', i, '-й пары: ', end='')
    n_list.append(int(input()))
k_list = []
k = int(input('Кол-во людей: '))
for i in range(1, k + 1):
    print('Размер ноги', i, '-го человека:', end='')
    k_list.append(int(input()))
sorted(n_list)
sorted(k_list)
count = 0
for human in k_list:
    for size in n_list:
        if human <= size:
            count += 1
            n_list.remove(size)
            break
print('Наибольшее кол-во людей, которые могут взять ролики:', count)