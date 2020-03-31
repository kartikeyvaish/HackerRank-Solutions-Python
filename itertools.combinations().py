from itertools import combinations

def Printing(a):
    for k in a:
        for j in k:
            print(j,end="")
        print("\r")



ch = list(input().split())
till = int(ch[1])
ar = list(ch[0])
ar.sort()
for i in range(1, till+1):
    arr = list(combinations(ar, i))
    Printing(arr)
    arr.clear()