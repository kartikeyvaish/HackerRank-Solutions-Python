n = int(input())
Countries = set()
for i in range(n):
    ch = input()
    Countries.add(ch)

print(len(Countries), end="")