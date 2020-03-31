if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
arr = []
for i in range(0,x):
    for j in range(0,y):
        for k in range(0,z):
                            if i+j+k!=n:
                                arr.append(i)
                                arr.append(j)
                                arr.append(k)

print(arr)