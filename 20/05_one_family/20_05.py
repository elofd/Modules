names = {
    ('Сидоров', 'Никита'): 35,
    ('Сидорова', 'Алина'): 34,
    ('Сидоров', 'Павел'): 10,
    ('Иванов', 'Петр'): 14,
    ('Иванова', 'Анна'): 43,
    ('Иванов', 'Сергей'): 15,
}
full_age = 0
family = input('Введите фамилию: ').lower()
for name, age in names.items():
    if family == name[0].lower() or family + 'а' == name[0].lower() or family[:-1] == name[0].lower():
        print(name[0], name[1], ':', age)
        full_age += age
print('Общий возраст:', full_age)
