n = (int(input()))
list = []
for i in range(1,n+1):
    d = input().split()
    if d[0] == 'insert':
        list.insert(int(d[1]) , int(d[2]))
    elif d[0] == 'print':
        print(list)
    elif d[0] == 'remove':
        list.remove(int(d[1]))
    elif d[0] == 'append':
        list.append(int(d[1]))
    elif d[0] == 'sort':
        list.sort()
    elif d[0] == 'pop':
        list.pop()
    elif d[0] == 'reverse':
        list.reverse()