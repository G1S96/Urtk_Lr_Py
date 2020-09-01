import math

a = []

for k in range(4):
    a.append([])
    for n in range(4):
        f = math.cos(2.1*(k+1))*math.sin(math.fabs(k)/0.15)-5.8
        g = math.fabs(math.cos((2*n)**3+2*math.sin(n/1.2)))+10.51*math.cos(math.fabs(3*n))
        akn = ((n+1)*f+math.sin(k+1)*g)
        a[k].append(round(akn))
    print(a[k])
print()

s = 0

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j]>=1 :
             s += a[i][j]**2
print("сумму квадратов больших 1: ",s)