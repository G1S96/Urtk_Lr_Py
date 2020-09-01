high = int(input('Введите количество элементов массива: '))
array = []
low = 0
for i in range(1, (high*2), 2):
    array.append(i**2)
    array.append(i**2)
print(array)

x = int(input('X: '))

while low < high:
    middle = (low + high) // 2
    if array[middle] < x:
        low = middle + 1
    else:
        high = middle
if array[high] == x:
    print('Элемент',high,'содержит значение', x)
else:
    print('Массив не содержит значение', x)
