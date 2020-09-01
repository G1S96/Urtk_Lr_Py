I = input
n = int(I())
a = I().count('A') * 2
print([['Friendship', 'Danik'][a < n], 'Anton'][a > n]) #62mc

input()
w = input()
a, b = map(w.count, ('A', 'D'))
print("Anton" if a > b else "Danik" if b > a else "Friendship") #77mc

n=int(input())
result=input()
dan = int(result.count('D'))
ant = int(result.count('A'))
if dan>ant:
    print('Danik')
elif ant>dan:
    print('Anton')
else:
    print('Friendship') #124mc
