input()
a, b, c = [sum(map(int, input().split())) for i in range(3)]
print (a - b)
print (b - c) #155mc

n = int(input())
s = [sum(map(int, input().split())) for i in range(3)]
print(s[0] - s[1])
print(s[1] - s[2]) #170mc

n = int(input())
n1 = sum(list(map(int, input().split())))
n2 = sum(list(map(int, input().split())))
n3 = sum(list(map(int, input().split())))
print(abs(n1-n2))
print(abs(n2-n3)) #218mc
