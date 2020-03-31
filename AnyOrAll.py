def PalinCheck(a):
    s = 0
    x = a
    while a > 0:
        rem = a % 10
        a = a // 10
        s = s * 10 + rem
    if s == x:
        return 1
    else:
        return 0


def Pos(a):
    if a > 0:
        return 1
    else:
        return 0


def Main():
    n = int(input())
    Numbers = list(map(int, input().split()))
    for i in Numbers:
        if PalinCheck(i) == 0 and Pos(i) == 0:
            return "False"
    return "True"

print(Main())

