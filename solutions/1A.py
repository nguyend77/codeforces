# https://codeforces.com/problemset/problem/1/A

import math

n, m, a = [int(x) for x in input().split()] # unpacking
print(math.ceil(n/a)*math.ceil(m/a))