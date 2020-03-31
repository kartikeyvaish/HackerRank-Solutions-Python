Set = set(map(int, input().split()))
Test = int(input())
R = 0
while Test != 0:
    Test = Test - 1
    Trial = set(map(int, input().split()))
    if Set.issuperset(Trial):
        R = 0
    else:
        R = 1
        break
    Trial.clear()


if R == 1:
    print("False", end="")
else:
    print("True", end="")