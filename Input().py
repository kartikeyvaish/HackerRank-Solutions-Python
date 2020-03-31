N, M = map(int, input().split())
sum = 0
K = M
M = M - 1
while M != -1:
    sum = sum + N**M
    M = M - 1
if sum == K:
    print("True", end="")
else:
    print("False", end="")