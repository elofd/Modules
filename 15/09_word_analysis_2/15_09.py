word = list(input('Введите слово: '))
flag = True
for i in range(len(word) // 2):
    if word[i] != word[len(word) - 1 - i]:
        flag = False
if flag:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
