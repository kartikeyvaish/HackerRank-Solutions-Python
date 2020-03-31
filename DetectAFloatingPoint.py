import re
for i in range(input()):
    k = input()
    print(bool(re.match(r'^[+-]?\d*?\.{1}\d+$',k)))