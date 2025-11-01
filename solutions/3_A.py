# https://codeforces.com/problemset/problem/3/A

def get_coordinates(position):
    x = ord(position[0]) - 96
    y = int(position[1])
    return (x,y)

start = get_coordinates(input())
finish = get_coordinates(input())

x_current = start[0]
y_current = start[1]
count = 0
steps = []
while x_current != finish[0] or y_current != finish[1]:
    while x_current < finish[0] and y_current < finish[1]:
        steps.append('RU')
        x_current += 1
        y_current += 1
        count += 1
    while x_current < finish[0] and y_current > finish[1]:
        steps.append('RD')
        x_current += 1
        y_current -= 1
        count += 1
    while x_current > finish[0] and y_current > finish[1]:
        steps.append('LD')
        x_current -= 1
        y_current -= 1
        count += 1
    while x_current > finish[0] and y_current < finish[1]:
        steps.append('LU')
        x_current -= 1
        y_current += 1
        count += 1
    while x_current < finish[0] and y_current == finish[1]:
        steps.append('R')
        x_current += 1
        count += 1
    while x_current > finish[0] and y_current == finish[1]:
        steps.append('L')
        x_current -= 1
        count += 1
    while x_current == finish[0] and y_current < finish[1]:
        steps.append('U')
        y_current += 1
        count += 1
    while x_current == finish[0] and y_current > finish[1]:
        steps.append('D')
        y_current -= 1
        count += 1
print(count)
for step in steps:
    print(step)