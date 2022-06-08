while True:
    up_count = 0
    num_count = 0
    password = input('Придумайте пароль: ')
    for symbol in password:
        if symbol.isupper():
            up_count += 1
        elif symbol.isdigit():
            num_count += 1
    if len(password) < 8 or up_count < 1 or num_count < 3:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        break
print('Это надёжный пароль!')