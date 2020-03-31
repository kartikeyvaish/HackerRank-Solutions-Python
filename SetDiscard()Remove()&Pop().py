def Pop(s):
    s.pop()
    return s


def Remove(s, a):
    s.remove(a)
    return s


def Discard(s, a):
    s.discard(a)
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
elem = 0
for i in range(t):
    ch = input()
    arr = list(ch.split())
    if arr[0] == "pop":
        s = Pop(s)
    elif arr[0] == "remove":
        if int(arr[1]) in s:
            s = Remove(s, int(arr[1]))
    elif arr[0] == "discard":
        if int(arr[1]) in s:
            s = Discard(s, int(arr[1]))

print(Sum(s),end="")

