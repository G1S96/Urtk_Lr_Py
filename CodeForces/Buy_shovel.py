k,r=map(int,input().split());i=1
while 0!=k*i%10!=r:
    i+=1
print(i) #62mc
 
 
k,r=map(int,input().split())
i=1
while k*i%10!=r and k*i%10!=0:
    i+=1
print(i) #77mc


k,r = map(int,input().split());k1=1;i=k
while True:
    if k%10==0 or (k-r)%10==0:
        print(k1)
        break
        if k%r==0:
            print(k//r)
            break
    k+=i
    k1+=1 #109mc
