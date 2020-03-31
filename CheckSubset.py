Test = int(input())
while Test != 0:
    Test = Test - 1
    SizeA = int(input())
    SetA = set(map(int, input().split()))
    SizeB = int(input())
    SetB = set(map(int, input().split()))
    print(SetA.issubset(SetB))
    SetA.clear()
    SetB.clear()