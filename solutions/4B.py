# https://codeforces.com/problemset/problem/4/B

d, sum_time = [int(x) for x in input().split()]

schedule = []
min = 0
max = 0
total_time = 0
for day in range(d):
    min_time, max_time = [int(x) for x in input().split()]
    min += min_time
    max += max_time
    total_time += min_time
    schedule.append({'min_time': min_time, 'max_time': max_time, 'spent_time': min_time})

if min > sum_time or max < sum_time:
    print('NO')
else:
    shortage = sum_time-total_time
    for day in schedule:
        while (shortage > 0) and (day['spent_time'] < day['max_time']):
                day['spent_time'] += 1
                shortage -= 1
    answer = [str(day['spent_time']) for day in schedule]
    print('YES')
    print(' '.join(answer))