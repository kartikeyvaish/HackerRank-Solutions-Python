from itertools import combinations_with_replacement


def Printing(a):
    for k in a:
        for j in k:
            print(j,end="")
        print("\r")


ch = list(input().split())
till = int(ch[1])
ar = list(ch[0])
ar.sort()
arr = list(combinations_with_replacement(ar, till))
Printing(arr)