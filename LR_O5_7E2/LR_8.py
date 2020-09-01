high = int(input('Введите количество элементов массива: '))
array = [1,1,9,9,15,15,49,49,81,81]
low = 0
print(array)

x = int(input('X: '))

while low < high:
    middle = (low + high + ) // 2
    if array[middle] < x:
        low = middle + 1
    else:
        high = middle
if array[high] == x:
    print('Элемент',high,'содержит значение', x)
else:
    print('Массив не содержит значение', x)
