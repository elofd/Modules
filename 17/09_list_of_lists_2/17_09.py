nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
print('Ответ:', [nice_list[i][j][_] for i in range(len(nice_list))
                 for j in range(len(nice_list[i]))
                 for _ in range(len(nice_list[i][j]))])

