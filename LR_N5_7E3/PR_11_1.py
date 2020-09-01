def digiroot(number):
    if (number == 0):return number
    return  number % 10 + digiroot(number//10)

def tottal_digiroot(number):
    res = digiroot(number)
    if (res // 10 == 0):return res
    return tottal_digiroot(res)
while(True):
    try:
        number = int(input("Enter value: "))
        break
    except ValueError:
        print("Incorrect input")

print("Root: ",tottal_digiroot(number))
