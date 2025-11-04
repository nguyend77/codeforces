# https://codeforces.com/problemset/problem/4/C

name_dict = {} # {username: count}
n = int(input())
for _ in range(n):
    user = input()
    if user not in name_dict.keys():
        name_dict[user] = 1
        print('OK')
    else:
        print(f'{user}{name_dict[user]}')
        name_dict[user] += 1