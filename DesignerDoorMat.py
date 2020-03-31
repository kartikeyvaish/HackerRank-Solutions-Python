N,M = input().split()
message = "WELCOME"
c=1
g=1
N= (int(N))
M= (int(M))
f=4
h=3
middlespace = M - len(message)
print(middlespace)
FirstCorner = (int(N/2)) * 3
till = FirstCorner
for mains in range(1,N+1):
    if mains<(N+1)/2:
        for i in range(1,till+1):
            print("-",end="")
        for i in range(1,g+1):
            print(".|.",end="")
        for i in range(1,till+1):
            print("-",end="")
        g=g+2

    if mains == (N+1)/2:
        for i in range(1,(int(middlespace/2))+1):
            print("-",end="")
        for i in range(0,len(message)):
            print(message[i],end="")
        for i in range(1,(int(middlespace/2))+1):
            print("-",end="")
        g=g-2

    if mains> (N+1)/2:
        for i in range(1,f):
            print("-",end="")
        for i in range(1,g+1):
            print(".|.",end="")
        for i in range(1,f):
            print("-",end="")
        g=g-2
        f=f+3

    print("\r")
    c=c+1
    till = till -3