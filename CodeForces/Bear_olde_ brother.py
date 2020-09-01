import math
a,b=map(int,input().split())
print(int(math.log(1.5*b/a,1.5))) # 63mc

import math
a,b=map(int,input().split())
print(int(math.log(b/a,1.5))+1) #93mc

x,y = map(int,input().split())
i=0
while x<=y:
    x=x*3
    y=y*2
    i+=1
print(i) #124mc
