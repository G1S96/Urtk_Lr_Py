k=0
for _ in range(int(input())):c,d=map(int,input().split());k+=c>d;k-=c<d
print('Mishka' if k>0 else ['Friendship is magic!^^','Chris'][k<0])
#62mc



mcount = 0
ccount = 0
# print ("Input n")
n = int(input())
for i in range(n):
    # print ("Input the next pair of scores, separated by a space")
    m,c = (int(x) for x in input().split())
    if m > c:
        mcount += 1
    elif m < c:
        ccount += 1
if mcount > ccount:
    print ("Mishka")
elif mcount < ccount:
    print ("Chris")
else:
    print ("Friendship is magic!^^") #77mc
    
  
  
    n = int(input())
Mishka = 0;Chris = 0
for i in range(n):
    m,c = map(int,input().split())
    if m>c:
        Mishka+=1
    elif c>m:
        Chris+=1
if Mishka>Chris:
    print('Mishka')
elif Chris>Mishka:
    print('Chris')
else:
    print('Friendship is magic!^^') #124mc
