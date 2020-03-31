def average(array):
    a=[]
    sum=0
    a=set(array)
    for i in a:
        sum = sum + i
    return (sum/len(a))
n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)