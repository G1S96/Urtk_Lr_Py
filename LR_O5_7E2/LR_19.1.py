import random
def del_min_max(a):
    return sorted(a, reverse=True)[1:len(a) - 1]


ass = tuple(random.randint(10, 100) for i in range(10))

print(*(del_min_max(ass)))

input(ass)