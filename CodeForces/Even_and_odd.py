n,k = map(int,input().split())
if n%2==0 and n//2<k:
    print(abs(((n//2)-k)*2))
elif n%2==0 and n//2>=k:
    print(k+(k-1))
elif n%2==1 and (n//2)+1<k:
    print(abs(((n+1)-k)-k))
else:
    print(k+(k-1))     #218mc

n,k=map(int,input().split())
d=n+1>>1
print((k*2-1,(k-d)*2)[k>d]) #46mc

a,b=map(int,input().split())
c=b-(a+1)//2
print([2*b-1,2*c][c>0])    #78mc
