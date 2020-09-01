def function(x, n, m):
    import math
    go = 0
    for j in range(n):
        for i in range(m, n + 1):
            go += x * 2 * i / math.factorial(2 * i)
    print(go)
function(7, 3, 3)

