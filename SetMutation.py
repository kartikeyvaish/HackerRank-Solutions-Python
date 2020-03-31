def IntersectionUpdate(s, a):
    s.intersection_update(a)
    return s


def Update(s, a):
    s.update(a)
    return s


def SymmetricDifferenceUpdate(s, a):
    s.symmetric_difference_update(a)
    return s


def DifferenceUpdate(s, a):
    s.difference_update(a)
    return s


def Sum(s):
    sum = 0
    for i in range(len(s)):
        ch = s.pop()
        sum = sum + ch

    return sum


n = int(input())
s = set(map(int, input().split()))
t = int(input())


for i in range(t):
    ch = list(input().split())
    if ch[0] == "intersection_update":
        a = set(map(int, input().split()))
        s = IntersectionUpdate(s, a)
    elif ch[0] == "update":
        a = set(map(int, input().split()))
        s = Update(s, a)
    elif ch[0] == "symmetric_difference_update":
        a = set(map(int, input().split()))
        s = SymmetricDifferenceUpdate(s, a)
    elif ch[0] == "difference_update":
        a = set(map(int, input().split()))
        s = DifferenceUpdate(s, a)

print(Sum(s), end="")