
# 12.5. Дан двумерный массив. Вывести на экран:
#       б) все элементы s-го столбца массива

lenX = int(input('Enter X: '))
lenY = int(input('Enter Y: '))

matrix = [[]] * lenX
for i in range(lenX):
    matrix[i] = [0] * lenY

for i in range(lenX):
    print(matrix[i])

import random

for i in range(lenX):
    for j in range(lenY):
        matrix[i][j] = random.randint(10, 99)

for i in range(lenX):
    print(matrix[i])

s = int(input('Enter column s: '))
for j in range(lenY):
    print(matrix[j][s-1])


# 12.6. Дан двумерный массив. Вывести на экран:
#       б) все элементы m-й строки массива.

m = int(input('Enter string m: '))
for i in range(lenX):
    print(matrix[m-1][i])


# 12.33.
#      Дан двумерный массив. Вывести на экран:
#      а) все элементы 5-го столбца массива, начиная с последнего
# элемента этого столбца;

for j in range(lenY-1, -1, -1):
    print(matrix[j][4])


# 12.62.
#      Дан двумерный массив. Найти:
#      а) сумму элементов каждой строки

summ = 0
index = 0
while index < lenY:
    for i in range(lenX):
        summ += matrix[index][i]
    print(summ)
    summ = 0
    index += 1


# 12.90.
#        Дан двумерный массив. В каждой его строке найти:
#        а) максимальный элемент;

index = 0

while index < lenY:
    maxNumber = matrix[index][0]

    for i in range(lenX):
        if matrix[index][i] > maxNumber:
            maxNumber = matrix[index][i]

    print(maxNumber)

    index += 1

#    б) минимальный элемент;

index = 0

while index < lenY:
    minNumber = matrix[index][0]
    for i in range(lenX):
        if matrix[index][i] < minNumber:
            minNumber = matrix[index][i]

    print(minNumber)

    index += 1
