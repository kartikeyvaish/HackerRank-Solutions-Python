a = int(input())
A = set()
arr = list(map(int, input().split()))
for i in arr:
    A.add(i)
b = int(input())
B = set()
arr = list(map(int, input().split()))
for i in arr:
    B.add(i)

Res = A.symmetric_difference(B)
arr.clear()
for i in range(len(Res)):
    arr.append(Res.pop())

arr.sort()

for i in arr:
    if i == arr[len(arr) - 1]:
        print(i,end="")
    else:
        print(i)