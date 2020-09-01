f=input
print(sum('+'in f()or-1 for i in range(int(f()))))#62mc

print(sum(input().count('+') - 1 for _ in range(int(input()))))#62mc

k=[]
for i in range(int(input())):
    su=input()
    k.append(su[1:2])
print((k.count('+'))-(k.count('-')))
#108mc

