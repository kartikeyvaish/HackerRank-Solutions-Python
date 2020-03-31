n = input()
arr = n.split()
arr = [int(i) for i in arr]
A = []
B = []
for i in range(0,arr[0]):
    A.append(input())
for i in range(0,arr[1]):
    B.append(input())
c=0
for i in range(0,len(B)):
    for j in range(0,len(A)):
        if B[i] == A[j]:
            c=c+1
    if c>0:
        for l in range(0, len(A)):
            if B[i] == A[l]:
                print(l+1,end=" ")
    else:
        print("-1",end="")

    c=0
    print("\r")