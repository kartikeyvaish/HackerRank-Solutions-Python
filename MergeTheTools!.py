def removeDupli(strings):
    ch = ""
    for i in range(0,len(strings)):
        if ch.count(strings[i]) == 0:
            ch = ch + strings[i]

    return ch

def merge_the_tools(string, k):
    size = len(string)
    parts = (int(size/k))
    arr = []
    c=""
    for i in range(0,size,3):
        for j in range(i,i+3):
            c = c + string[j]
        arr.append(c)
        c=""

    for i in range(0,len(arr)):
        c = removeDupli(arr[i])
        print(c)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
