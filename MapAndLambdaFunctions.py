cube = lambda x: x*x*x


def fibonacci(n):
    a = -1
    b = 1
    c = 0
    Res = []
    for i in range(n):
        c = a + b
        a = b
        b = c
        Res.append(c)
    return Res


n = int(input())
print(list(map(cube, fibonacci(n))))