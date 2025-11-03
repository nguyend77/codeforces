# https://codeforces.com/problemset/problem/3/C

def check_winner(matrix, player): # player = 'X' or '0'
    condition = [player, player, player]
    if player == 'X':
        result = 'the first player won'
    else:
        result = 'the second player won'
    for row in matrix: # horizontal line
        if row == condition:
            return result
    for columnn in range(3): # vertical line
        if [matrix[x][columnn] for x in range(3)] == condition:
            return result
    if [matrix[i][i] for i in range(3)] == condition or [matrix[i][2-i] for i in range(3)] == condition:
        return result
    return '' # player did not win

def check_finished(matrix):
    for row in matrix:
        for i in row:
            if i == '.':
                return False
    return True

grid = [[],[],[]] # initialize empty grid
count_x = 0
count_o = 0
for i in range(3): # 3x3 grid
    for char in input():
        grid[i].append(char)
        if char == 'X':
            count_x += 1
        elif char == '0':
            count_o += 1
x_win = check_winner(grid, 'X')
o_win = check_winner(grid, '0')

if (count_x < count_o) or (count_x > count_o+1) or (x_win and o_win) or (x_win and count_x != count_o + 1) or (o_win and count_x != count_o):
    print('illegal')
else:
    if x_win:
        print(x_win)
    elif o_win:
        print(o_win)
    else:
        if check_finished(grid):
            print('draw')
        else:
            if count_x > count_o:
                print('second')
            elif count_x == count_o:
                print('first')