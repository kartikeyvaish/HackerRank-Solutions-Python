from itertools import combinations

def Printing(a):
    A = 0
    Total = len(a)
    for j in a:
        if 'a' in j:
            A = A + 1
    print(round( (A/Total), 4))


n = int(input())
ch = list(input().split())
k = int(input())
arr = list(combinations(ch, k))
Printing(arr)