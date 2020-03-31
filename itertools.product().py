from itertools import product
mains = []
a = input()
c=0
arr1 = a.split()
arr1 = [int(i) for i in arr1]
a = input()
arr2 = a.split()
arr2 = [int(i) for i in arr2]
mains.append(list(product(arr1,arr2)))

for i in range(0, len(arr1) * len(arr2)):
    print(mains[0][c],end=" "
    c=c+1