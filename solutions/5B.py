# https://codeforces.com/problemset/problem/5/B

lines = []
max_length = 0
left = True
try:
    while True:
        text = input()
        lines.append(text)
        if len(text) > max_length:
            max_length = len(text)
except EOFError:
    pass
print('*' * (max_length+2))
for text in lines:
    buffer = max_length - len(text)
    if buffer % 2 == 0:
        print('*' + ' '*(buffer//2) + text + ' '*(buffer//2) + '*')
    else: # alternate between left and right
        if left:
            print('*' + ' '*(buffer//2) + text + ' '*(buffer//2 + 1) + '*')
        else:
            print('*' + ' '*(buffer//2 + 1) + text + ' '*(buffer//2) + '*')
        left = not left
print('*' * (max_length+2))