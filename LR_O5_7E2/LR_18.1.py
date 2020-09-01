permissions = {}
n = int(input())
for _ in range(n):
    s = input().split()
    permissions[s[0]] = set(s[1:])
for _ in range(int(input())):
        perm,file = input().split()
        if perm == 'read':
            perm = 'R'
        if perm == 'write':
            perm = 'W'
        if perm == 'execute':
            perm = 'X'
        if perm in permissions[file]:
            print('OK')
        else:
            print('Access denied')

'''
4
helloworld.exe R X
pinglog W R
nya R
goodluck X W R
5
read nya
write helloworld.exe
execute nya
read pinglog
write pinglog
'''