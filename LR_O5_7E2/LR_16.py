#5
a = input("Введите натуральное число: ")
print("позиция:",a.index(min(a))+1,"минимальная цифра: ",min(a))


#16
g = map(int,str(a))
max = a[0]
pos = 0
for i in range(len(a)):
    if i%2==0:
        if a[i]>max: max=a[i];pos=i
print ("максимальня четная: ",max,", позиция: ",pos+1)