# https://codeforces.com/problemset/problem/2/B

def factor(p,a): # find the power of p in factorization of a
    if a==0:
        return 1
    count = 0
    while a>0 and a % p == 0:
        count += 1
        a = a//p
    return count
    
def game(p,matrix,size):
    cost = [[0 for _ in range(size)] for _ in range(size)] # new matrix for cost along paths
    cost[0][0] = factor(p, matrix[0][0]) # starting position
    for i in range(1,size):
        cost[i][0] = cost[i-1][0] + factor(p, matrix[i][0]) # positions along outer column
    for j in range(1,size):
        cost[0][j] = cost[0][j-1] + factor(p,matrix[0][j]) # positions along upper row
    for i in range(1,size):
        for j in range(1,size):
            cost[i][j] = min(cost[i-1][j], cost[i][j-1]) + factor(p, matrix[i][j]) # can either go down or right
    min_cost = cost[size-1][size-1]
    path_reversed = '' # find shortest path from destination back to origin
    i = size-1
    j = size -1
    for step in range(2*size-2,0,-1): # 2n-2 steps total
        if i>0 and j>0:
            if cost[i-1][j] < cost[i][j-1]:
                path_reversed += 'D'
                i -= 1
            else:
                path_reversed += 'R'
                j -= 1
        elif i==0 and j>0:
            path_reversed += 'R'
            j -= 1
        elif i>0 and j==0:
            path_reversed += 'D'
            i -= 1
    path = path_reversed[::-1]
    return (min_cost,path)

def find_zero(matrix, size):
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 0:
                return True
    return False

def path_zero(matrix, size):
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 0:
                return f"1\n{'D'*i + 'R'*(n-1) + 'D'*(n-i-1)}"

n = int(input()) # n*n matrix
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])
game2 = game(2,matrix,n)
game5 = game(5,matrix,n)
if not find_zero(matrix, n):
    if game2[0] <= game5[0]:
        print(game2[0])
        print(game2[1])
    else:
        print(game5[0])
        print(game5[1])
else:
    if game2[0] <= game5[0] and game2[0] <= 1:
        print(game2[0])
        print(game2[1])
    elif game5[0] < game2[0] and game5[0] <= 1:
        print(game5[0])
        print(game5[1])
    else:
        print(path_zero(matrix,n))