from collections import OrderedDict
n=int(input())
ch = ""
Data = {}
for i in range(n):
    ch = input()
    List = list(ch.split())
    ToAdd = List[len(List)-1]
    List.remove(ToAdd)
    ch = ' '.join(List)
    if ch in Data:
        Data[ch] = Data[ch] + int(ToAdd,10)
    else:
        Data[ch] = int(ToAdd,10)



for i in Data.items():
    print(i[0],' ',i[1])