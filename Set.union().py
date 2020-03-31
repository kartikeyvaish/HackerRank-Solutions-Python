a = int(input())
A = set()
arr = list(map(int, input().split()))
for i in range(len(arr)):
    A.add(arr[i])
b = int(input())
B = set()
arr = list(map(int, input().split()))
for j in range(len(arr)):
    B.add(arr[j])
print(len(A.union(B)))