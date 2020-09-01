a, b = input(), input()
s = str(int(a) + int(b)).replace("0", "")
if int(a.replace("0", "")) + int(b.replace("0", "")) == int(s):
	print("YES")
else:
	print("NO") #124mc
  
  a = input()
b = input()
a_o = int(a.replace('0',''))
b_o = int(b.replace('0',''))
s = int(str(int(a)+int(b)).replace('0',''))
 
print (('NO','YES')[(a_o+b_o) == s]) #124mc

a = input();b = input();c=int(a)+int(b)
if int(a.replace('0',''))+int(b.replace('0',''))==int(str(c).replace('0','')):print('YES')
else:print('NO') #248mc
