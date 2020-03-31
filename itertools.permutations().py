from itertools import permutations
arr = []
c=0
e=[]
permut = []
string = input()
b=string.split()
str = b[0]
e.append(b[1])
e = [int(i) for i in e]
for i in range(0,len(b[0])):
    arr.append(str[i])

permut = list(permutations(arr,e[0]))
permut.sort()

for i in range(0,len(permut)):
    d = permut[i]
    for j in range(0,e[0]):
        print(d[j],end="")
    print("\r")