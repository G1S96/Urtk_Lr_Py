n = int(input('Введите размерность матрицы -> '))

a=[]
for i in range(n):
    a.append([0]*n)

for i in range(n):
    for j in range(n):
        if (j==0 or i==0 or j==n-1 or i==n-1):
            a[i][j]=1

for i in a:
    print(*i)

print("____________________\n")

matrix = [[1 if (x==0 or y==0 or x==n-1 or y==n-1) else 0 for x in range(n)] for y in range(n)]

for line in matrix:
    print(*line)
