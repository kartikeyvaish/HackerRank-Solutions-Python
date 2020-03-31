n=(int(input()))
elem=0
A = set()
B = set()
for i in range(0,n):
    elem=(int(input()))
    A.add(elem)

m=(int(input()))
for i in range(0,m):
    elem=(int(input()))
    B.add(elem)

myset = A.intersection(B)

for i in myset:
    A.discard(i)
for i in myset:
    B.discard(i)
A = A.union(B)
FinalRes = list(A)
newlis = list(map(int, FinalRes))
newlis.sort()
for i in newlis:
    print(i)