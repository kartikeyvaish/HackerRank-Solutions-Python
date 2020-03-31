import numpy
#1 2 3 4 -8 -10

def arrays(arr):
    return (numpy.array(arr[::-1], float))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)