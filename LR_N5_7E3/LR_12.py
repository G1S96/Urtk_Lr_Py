high = int(input('Введите количество элементов массива: '))

array = []
step =0
for i in range(1,high+1,2):
    if step % 2 !=0 or i==1:
        array.append(i*i)
    else:
        array.append(i*3)
    step+=1


b = []
for i in array:
    b.extend([i, i])

if high %2 ==0:
    print(*b)
else:
    print(*b[:-1])


low = 1
x = int(input('$: '))


while low < high:
    middle = (low + high) // 2

    if b[middle] < x:
        low = middle + 1
    else:
        high = middle
if b[high] == x:

    print('Элемент',high + 1,'содержит значение', x)
else:
    print('Массив не содержит значение', x)
