def swap_case(s):
    c=""
    for i in range(0,len(s)):
        if ord(s[i]) >= 65 and ord(s[i]) <= 90:
            c = c + chr(ord(s[i]) + 32)

        elif ord(s[i]) >= 97 and ord(s[i]) <= 122:
            c = c + chr(ord(s[i]) - 32)

        else:
            c=c+ chr(ord(s[i]))

    return c

str = input()
result = swap_case(str)
print(result)