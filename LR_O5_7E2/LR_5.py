import random,math
arr = []
a = []
b = []
for  i in range(15):
    a.append(random.randint(1,10))
    b.append(random.randint(1, 10))
for i in range (15):
    arr.append(math.sqrt(abs((a[i]**3)-(b[i]**2))))
List = [ round(elem, 2) for elem in arr]
print(a,b,end="\n")
print(List)
print(max(List))
print(min(List))