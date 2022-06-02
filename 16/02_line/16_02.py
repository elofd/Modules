cl_1 = list(range(160, 177, 2))
cl_2 = list(range(162, 181, 3))
cl_1.extend(cl_2)
print('Отсортированный список учеников', sorted(cl_1))