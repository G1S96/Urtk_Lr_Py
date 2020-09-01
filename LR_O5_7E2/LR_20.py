import random
def ass(pol):
    let = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz'
    sym = '()-/\*,.;:`!@#$%^&'
    num = '0123456789'
    eve = '0123456789()-/\*,.;:`!@#$%^&ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz'
    password = ''
    counter=0
    for i in range(pol):
        counter+=1
        if counter==1:
            password+=random.choice(let)
        if counter==2:
            password+=random.choice(sym)
        if counter==3:
            password+=random.choice(num)
        if counter>3:

            password+=random.choice(eve)
    return print(password)

pol = int(input('введите длинну пароля'))
ass(pol)