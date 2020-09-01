p=m=0
for _ in range(int(input())):
  a,b=map(int,input().split())
  p=p-a+b;m=max(m,p)
print(m) #124mc


n=int(input())
r,c=0,0
for i in range(n):
 a,b=map(int,input().split())
 c+=b-a
 r=max(r,c)
print(r) #124mc


k=0;k1=[]
for _ in range(int(input())):
    n,m = map(int,input().split())
    k-=n
    k+=m
    k1.append(k)
print(max(k1)) #248
