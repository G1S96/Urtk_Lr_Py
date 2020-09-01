def CountSquare(a,b,n):
    if a == b:
        return n + 1
    if (a < b):
        return CountSquare(a, b - a, n + 1)
    return CountSquare(a - b, b, n + 1)



n = 0
a = int(input("A = "))
b = int(input("B = "))
print(CountSquare(a,b,n))