n = int(input('Введите длину списка: '))
numbers = [(1 if x % 2 == 0 else x % 5) for x in range(n)]
print(numbers)