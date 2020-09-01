import random

N = int(input("Введи число от 1000: $"))
k = 0
for i in range(N):
    x = random.uniform(0, 6)
    y = random.uniform(-6, 6)
    if 0<=x<=6 and x**2+y**2<=36 and y>=(x-6):k+=1
print(round(k/N*72,3))


