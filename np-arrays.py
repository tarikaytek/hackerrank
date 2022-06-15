# https://www.hackerrank.com/challenges/np-arrays/problem

import numpy


def arrays(arr):
    return numpy.array([float(i) for i in arr[::-1]])


arr = '1 2 3 4 -8 -10'.strip().split(' ')
result = arrays(arr)
print(result)
