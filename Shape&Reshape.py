import numpy

def arrays(arr):
    my_array = numpy.array(arr)
    lis = list(map(int, my_array))
    return numpy.reshape(lis, (3, 3))


arr = input().strip().split()
result = arrays(arr)
print(result)