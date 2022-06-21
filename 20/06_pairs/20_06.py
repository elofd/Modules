import random
numbers = [random.randint(0, 10) for x in range(10)]
print(numbers)
count = 0
numbers1 = [(numbers[index - 1], numbers[index]) for index, sym in enumerate(numbers) if index % 2 != 0]
print(numbers1)
numbers2 = [(numbers[index], numbers[index + 1]) for index, sym in enumerate(numbers) if index % 2 == 0]
print(numbers2)


