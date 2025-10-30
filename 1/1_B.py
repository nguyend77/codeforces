# https://codeforces.com/problemset/problem/1/B

def is_excel(input_str):
    for i in range(len(input_str)):
        try:
            if input_str[i].isdigit() and input_str[i+1].isalpha():
                return False # excel coordinates have no letter after digit
        except:
            pass
    return True

def to_excel(rxcy):
    c_index = rxcy.index('C') # r_index is 0
    row = int(rxcy[1:c_index])
    column_num = int(rxcy[c_index+1:len(rxcy)])
    str_reveresed = ''
    while column_num > 0:
        column_num -= 1
        remainder = column_num % 26
        str_reveresed += chr(remainder + 65)
        column_num = column_num // 26
    column_str = str_reveresed[::-1]
    print(f'{column_str}{row}')

def to_rxcy(excel):
    for i in range(len(excel)):
        if excel[i].isdigit():
            break # find index of first row number digit
    row = int(excel[i:])
    column_str = excel[:i]
    column = 0
    for position in range(len(column_str)):
        column += (ord(column_str[position])-64)*(26**(len(column_str)-position-1))
    print(f'R{row}C{column}')

n = int(input()) #number of test coordinates
for test in range(n):
    coordinate = input()
    if is_excel(coordinate):
        to_rxcy(coordinate)
    else:
        to_excel(coordinate)