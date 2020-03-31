import textwrap

def wrap(string, max_width):
    c = textwrap.fill(string,4)
    return c

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result,end="")



'''import textwrap

def wrap(string, max_width):
    remain = len(string) - len(string) % max_width
    for i in range(0,remain,max_width):
        for j in range(i,i+max_width):
            if j == ((i+max_width) -1):
                print(string[j])
            else:
                print(string[j],end="")
    if remain!=0:
        for i in range(remain,len(string)):
            print(string[i],end="")

if __name__ == '__main__':
    c=0
    string, max_width = input(), int(input())
    wrap(string, max_width)'''