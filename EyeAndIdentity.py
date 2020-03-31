import numpy
A = list(map(int, input().split()))
numpy.set_printoptions(sign=' ')
print(numpy.eye(A[0], A[1], k=0))