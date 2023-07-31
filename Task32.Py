list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
list_2 = []
max = 15
min = 5

for i in range(len(list_1)):
    if min <= list_1[i] <= max:
     print(i, end='')