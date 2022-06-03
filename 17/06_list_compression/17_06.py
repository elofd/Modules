import random
n = int(input('Количество чисел в списке: '))
nums = [random.randint(0, 2) for x in range(n)]
print('Список до сжатия', nums)
nums = [x for x in nums if x > 0]
print(nums)
