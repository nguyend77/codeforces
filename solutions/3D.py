# https://codeforces.com/problemset/problem/3/D

import heapq # for quick priority queue operations

sequence = [char for char in input()]

count_open = 0
count_close = 0
cost = 0
heap = []

if sequence[0] == ')' or sequence[-1] == '(': # check for impossible cases
    print(-1)
else:
    for i in range(len(sequence)):
        if sequence[i] == '(':
            count_open += 1
        elif sequence[i] == ')':
            count_close += 1
        else: # sequence[i] == '?'
            cost_open, cost_close = [int(x) for x in input().split()]
            heapq.heappush(heap, (cost_open-cost_close, i))
            sequence[i] = ')' # try choosing ')'
            count_close += 1
            cost += cost_close
        if  count_open < count_close and heap: # count of ')' must never be greater than '('
            if (heap[0][1] == len(sequence) - 1) and (len(heap) > 1): # avoid changing last character to '('
                heapq.heappop(heap)
            cheapest = heapq.heappop(heap) # remove used cheapest position
            sequence[cheapest[1]] = '(' # switch cheapest position to '('
            cost += cheapest[0]
            count_open += 1
            count_close -= 1
    if count_open != count_close:
        print(-1)
    else:
        print(cost)
        print(''.join(sequence))