import random


def C(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return C(n - 1, k) + C(n - 1, k - 1)

#n, k = map(int, input('').split())
while True:
    n = int(input("Из скольки элементов состоит  сочетание:"))
    k = int(input("По сколько элементов состоит  сочетание:"))
    if n == 0 : break
    print("Сочетание из", n, "элементов по", k, ":",  C(n, k))


def getX0(A):
    print("+++++++++++++++++++++++++++++++++++")
    import math as m
    if A < 0:
        X0 = m.sin(4 * A + m.cos(A))
    if 0 <= A < 3:
        X0 = m.sqrt(m.pow(A,2)+A)
    if A >= 3:
        X0 = m.cos(A + 1)
    return X0


X0 = getX0(random.randint(-25, 25))
print('getX0 =', X0)


def getXn(n):
    import math as m
    if n == 1:
        return X0
    Xn = m.sin(getXn(n-1)+2)+m.pow((getXn(n-1)/4),2)
    return Xn


for n in range(1, 16):
    print('getX', n, '=', getXn(n))
