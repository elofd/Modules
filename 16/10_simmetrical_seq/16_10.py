import time
n = int(input('Кол-во чисел: '))
numbers = []
for i in range(1, n + 1):
    numbers.append(int(input('Число: ')))
print('Последовательность:', numbers)
temp_numbers = []
temp_numbers.extend(numbers)
while True:
    count = 0
    for i in range(len(temp_numbers) // 2):
        if temp_numbers[i] != temp_numbers[len(temp_numbers) - 1 - i]:
            break
        count += 1
    if count > (len(temp_numbers) // 2 - 1):
        break
    new_numbers = []
    for i in range(count + 1):
        new_numbers.insert(0, numbers[i])
    temp_numbers = []
    temp_numbers.extend(numbers)
    temp_numbers.extend(new_numbers)
    print(temp_numbers, new_numbers, numbers)
    time.sleep(2)
print('Нужно приписать чисел:', len(new_numbers))
print('Сами числа:', new_numbers)
