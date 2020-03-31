Test = int(input())
for i in range(Test):
    ch = list(input().split())
    try:
        a = int(ch[0])
        b = int(ch[1])
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as v:
        print("Error Code:", v)