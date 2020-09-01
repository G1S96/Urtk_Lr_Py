from random import random

M = int(input('введите кол-во столбцов '))
N = int(input('введите кол-во строк '))
print('  ________________________')
mtx = []
arr = [0] * N * M
sumMain = 0
sumSecondary = 0
for i in range(N):
    a = []
    for j in range(M):
        a.append(int(random() * 10))
    mtx.append(a)

open("mtx 1.txt", 'w').write("\n".join(map(str, mtx)))
print("Первый список")
print((", ".join(map(str, mtx))))
print('  ________________________')

for i in range(N):
    for j in range(M):
        if mtx[i][j]==0:
            mtx[i][j]=1
        print("%3d" % mtx[i][j], end='')
    print()
for i in range(N):
    sumMain += mtx[i][i]
    sumSecondary += mtx[i][N - i - 1]
print('  ________________________')
open("mtx2.txt", 'w').write("\n".join(str(mtx)))
print ("Второй список")
print ((", ".join(map(str, mtx))))
print('  ________________________')
print("сумма элементов главной диагонали ",sumSecondary)
ile = open('mtx2.txt', 'r')
ile.read()
