import random

N = 15
array = []
for i in range(N):
    array.append(int(random.randrange(0, 50,2)))
array.sort()
print(array)


number = int(input("Enter the number: "))


low = 0
high = N-1
count=0

while low <= high:
    mid = (low + high) // 2
    if number < array[mid]:
        high = mid - 1
    elif number > array[mid]:
        low = mid + 1
    else:

        for i in array:
            if i == number:
                count+=1
        print ('Number',number,"quantity:",count,"ID =", mid+1)
        break
else:
    print("No the number")