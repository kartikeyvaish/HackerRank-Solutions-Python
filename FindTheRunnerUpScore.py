n = int(input())
arr =[]
swapped=1
for i in range (1,n+1):
    data = raw_input()
    arr.append(data)

arr.sort()
arr.reverse()

for i in range(0,n):
    if arr[i]!=arr[0]:
        print(arr[i])
        break