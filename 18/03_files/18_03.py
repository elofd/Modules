message = input('Название файла: ')
symbols = '@№$%^&\*()'
end = ['.txt', '.docx']
flag = True
for x in symbols:
    if message.startswith(x):
        print('Ошибка: название начинается на один из специальных символов.')
        flag = False
if flag:
    for i in end:
        if message.endswith(i):
            flag = True
            break
        else:
            flag = False
if flag:
    print('Файл назван верно.')
else:
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
