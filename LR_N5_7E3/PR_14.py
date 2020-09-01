from random import randint
def del_min_max(n):
    return sorted(n,reverse=True)[1:len(n)-1]

info_ball = tuple(randint(5,90)for i in range(10))
print(*(del_min_max(info_ball)))
