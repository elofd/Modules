import random
n = int(input('Введите максимальное число: '))
artem = random.randint(1, n)
flag = True
art_numbers = set(x for x in range(1, n + 1))
print(artem)
while flag:
    print(art_numbers)
    new_flag = True
    numbers = input('Нужное число есть среди вот этих чисел: ').split()
    if numbers == ['Помогите!']:
        print('Артём мог загадать следующие числа:', art_numbers)
        break
    nums = set(int(x) for x in numbers)
    if len(nums) > 1:
        for i in nums:
            if i == artem:
                print('Ответ Артёма: Да')
                art_numbers = art_numbers & set(nums)
                new_flag = True
                break
            else:
                new_flag = False
        if new_flag == False:
            print('Ответ Артёма: Нет')
    else:
        if nums[0] == artem:
            print('Ответ Артёма: Да')
            flag = False
        else:
            print('Ответ Артёма: Нет')



