from random import randint
n = 20
A = [randint(-7, 10) for i in range(n)]

for i in A:
    if i<0:
        with open('file2.txt', 'w', encoding='utf-8') as g:
            g.write("Нет положительных чисел")
            with open('file2.txt', 'r+', encoding='utf-8') as g:
                print(g.read())

open("A.txt", 'w').write("\n".join(map(str, A)))
print("Первый список")
print ((", ".join(map(str, A))))
pos = []
for i in A:
    if i>0:
        pos.append(i)

open("B.txt", 'w').write("\n".join(str(pos)))
print ("Второй список")
print ((", ".join(map(str, pos))))

d = min(pos)
b =(pos.index(d)+1)
print(len(pos),'элименов')
print(b,'- ',d)