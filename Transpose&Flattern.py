import numpy

n, m = map(int, input().split())
matrix = []
for i in range(n):
    a =[]
    a=list(map(int,input().split()))
    matrix.append(a)

print(numpy.transpose(matrix))
my_array = numpy.array(matrix)
print(my_array.flatten())