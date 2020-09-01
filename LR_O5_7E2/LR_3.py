import math
xn = float(input("Введите значение  нач: "))
xk = float(input("Введите значение  кон: "))
dx = float(input("Введите шаг шаг: "))

print("Таблица функций")
if dx == 0:
    print("Ошибка")
else:
    while xn!=xk+1:
        if  -10<= xn<0:
            y = (-3- xn / 2)
            print("X = ",xn," Y = ",y)
        if 0<=xn<3:
            y = -math.sqrt(3*3-(xn-0)*(xn-0))
            print("X = ", xn, " Y = ", y)
        if  3<=xn<=6:
            y = math.sqrt(3 * 3 - (xn - 6) * (xn - 6))
            print("X = ", xn, " Y = ", y)
        xn += dx
