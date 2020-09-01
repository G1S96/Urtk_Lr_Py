number = int(input('число'))
def sumdigits(number):
  if number == 0:
    return 0
  else:
    return (number%10) + sumdigits(number//10)
print('сумма:',sumdigits(number))