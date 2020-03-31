from _collections import deque

d = deque()
n = int(input())
for i in range(n):
    ch = input()
    q = list(ch.split())
    if(len(q) > 1):
        q[1] = int(q[1], 10)
    if q[0] == 'append':
        d.append(q[1])
    elif q[0] == 'pop':
        d.pop()
    elif q[0] == 'popleft':
        d.popleft()
    elif q[0] == 'appendleft':
        d.appendleft(q[1])
for i in d:
    print(i,end=" ")