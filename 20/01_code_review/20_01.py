students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}
def group(stud):
    all_interests = []
    long = 0
    for key, value in stud.items():
        for interest in value['interests']:
            all_interests.append(interest)
        long += len(value['surname'])
    return all_interests, long
all_interests_of_studs, long = group(students)
pairs = [(key, value['age']) for key, value in students.items()]
print('Список пар "ID студента — возраст":', pairs)
print('Полный список интересов всех студентов:', all_interests_of_studs)
print('Общая длина всех фамилий студентов:', long)