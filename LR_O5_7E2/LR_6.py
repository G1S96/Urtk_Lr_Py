from random import random
N = 5
arr = []
m =[]
for i in range(N):
    arr.append(int(random() * 100) - 50)
print(arr)

num = 0
for i in range(1,N):
    if abs(arr[i])>abs(arr[num]):
        num = i
        max = abs(arr[i])
print('max',max)
print('nomer',num+1)
into = False
result = 0
for i in arr:
    if i > 0:
        if into:
            into = False
            break
        else:
            into = True
    elif i < 0 and into:
        result += i
else:
    result='None'

print(result)
