n = (int(input()))
c=n-1
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Selected = ""
Reversed = ""
for i in range(0,n):
    Selected = Selected + a[i]
for i in range(0,n):
    Reversed = Reversed + Selected[n-1-i]
print(Selected)
print(Reversed)
till = (n*2)
Part1Dash = till -1
Part2Dash = 2
start =2
for i in range(1,n+1):
    for j in range(1,Part1Dash):
        print("- ",end="")
    for j in range(0,i):
        if i==1:
            print(Reversed[j],end=" ")
        else:
            print(Reversed[j],end=" - ")
    if i>1:
        for j in range(c,n):
            if j==(n-1):
                print(Selected[j],end=" ")
            else:
                print(Selected[j],end=" - ")
        c=c-1

    for j in range(1,Part1Dash):
        print("- ",end="")
    Part1Dash = Part1Dash - 2
    print("\r")

for i in range(1,n):
    for j in range(1,Part2Dash+1):
        print("- ", end="")
    for j in range(0,n-i):
        if i==n-1:
            print(Reversed[j],end=" ")
        else:
            print(Reversed[j], end=" - ")
    for j in range(start,n):
        if j==n-1:
            print(Selected[j],end=" ")
        else:
            print(Selected[j],end=" - ")
    for j in range(1,Part2Dash+1):
        print("- ",end="")
    start = start + 1
    Part2Dash = Part2Dash + 2
    print("\r")