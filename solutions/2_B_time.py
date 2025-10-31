# https://codeforces.com/problemset/problem/2/B
# code works, timie limit exceeded on test 7 

from itertools import permutations

def trailing_zeros(a):
    if a == 0:
        return 0
    elif a%10 != 0:
        return 0
    else:
        return 1 + trailing_zeros(a/10)

def product(matrix, path):
    a = 0 # row index
    b = 0 # column index
    result = matrix[0][0]
    for step in path:
        if step == 'D':
            a += 1
        else:
            b += 1
        if matrix[a][b] == 0:
            return 0
        else:
            result *= matrix[a][b]
    return result

n = int(input()) # n*n matrix
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])
sample = ['D'] * (n-1) + ['R'] * (n-1)
paths = set(permutations(sample)) # generate all possible paths
output = (8000,'') # (least # of trailing zeros, path)
for path in paths:
    num_zeros = trailing_zeros(product(matrix, path))
    if num_zeros < output[0]:
        output = (num_zeros, path)
print(output[0])
print(''.join(output[1]))