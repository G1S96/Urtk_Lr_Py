n=int(input())
ans=0
dec=1
while(n>=dec):
    n-=dec
    ans+=1
    dec+=ans+1
print(ans)  #61mc

n=int(input())
i=1
sum=1
 
while n>sum:
    i+=1
    sum+=(i*(i+1))/2
 
if n<sum:
    i-=1
 
print(i) #41mc
