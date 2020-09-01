import random
add=['STOL','STUL','TABUTETKA','DIVAN','TAHTA',
     'SHKAF','SHIFONER','PUFIK','TUMBA','KRESLO'
    ]
s1=set()
s2=set()
s3=set()
s4=set()
s5=set()
for i in range(4):
    s1.add(random.choice(add))
    s2.add(random.choice(add))
    s3.add(random.choice(add))
    s4.add(random.choice(add))
    s5.add(random.choice(add))
print("s1=",s1)
print("s2=",s2)
print("s3=",s3)
print("s4=",s4)
print("s5=",s5)
a=s1.intersection(s1,s2,s3,s4,s5)
print("Находится во всех множествах ", a)
y=set(add)
b=y.difference(s1,s2,s3,s4,s5)
print("не входят ни в одно множество", b)
c=y.intersection(s1,s2,s3)
print("входит в множетели s1 s2 s3", c)