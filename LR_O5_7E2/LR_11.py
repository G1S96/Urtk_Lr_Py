import random
n = int(input("Введите размерность матрицы: "))
def Mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print("{:4d}".format(mat[i][j]), end="")
        print()
    print()


a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = random.randint(10, 100)
Mat(a)
print("====================")
Mat(a[::-1])

# сортировка от лев
'''print("====================")
for i in range(n-1,-1,-1):
    for j in range(0,n,1):
        print(a[i][j],end="  ")
    print()'''
print('====================')
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==n-i+2:
            i=0
        print("{:3d}".format(i),end=' ')
    print()