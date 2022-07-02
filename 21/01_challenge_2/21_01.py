def run(number, count):
    if count == number:
        print(number)
        return
    print(count)
    count += 1
    run(number, count)

num = int(input('Введите num: '))
run(num, 1)