from _collections import deque
for t in range(int(input())):
    n = int(input())
    Sizes = list(map(int, input().split()))
    l = len(Sizes)
    i = 0
    while i < l - 1 and Sizes[i] >= Sizes[i+1]:
        i += 1
    while i < l - 1 and Sizes[i] <= Sizes[i+1]:
        i += 1

    if i == l-1:
        print("Yes")
    else:
        print("No")
