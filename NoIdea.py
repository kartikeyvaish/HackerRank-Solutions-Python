n = list(map(int, input().split()))
sum = 0
Array = list(map(int, input().split()))
SetA = set(map(int, input().split()))
SetB = set(map(int, input().split()))
for i in Array:
    if i in SetA:
        sum = sum + 1
    elif i in SetB:
        sum = sum - 1

print(sum)