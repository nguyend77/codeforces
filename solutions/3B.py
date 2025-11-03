# https://codeforces.com/problemset/problem/3/B
 
n, v = [int(x) for x in input().split()] # unpacking
kayaks = []
catamarans = []
for i in range(n):
    space, capacity = [int(x) for x in input().split()]
    if space == 1:
        kayaks.append((i+1, capacity))
    else:
        catamarans.append((i+1, capacity))
kayaks.sort(key = lambda item: item[1], reverse=True) # sort based on capacity
catamarans.sort(key = lambda item: item[1], reverse=True) # sort based on capacity
kayak_sum = [0] * (len(kayaks) + 1) # capacity of the best k kayaks
for i in range(len(kayaks)):
    kayak_sum[i+1] = kayak_sum[i] + kayaks[i][1]
catamaran_sum = [0] * (len(catamarans) + 1) # capacity of the best c catamarans
for i in range(len(catamarans)):
    catamaran_sum[i+1] = catamaran_sum[i] + catamarans[i][1]

optimal = 0
best_k = 0
best_c = 0
for k in range(min(v, len(kayaks))+1):
    c = min((v-k)//2, len(catamarans))
    max_capacity = kayak_sum[k] + catamaran_sum[c]
    if max_capacity > optimal:
        optimal = max_capacity
        best_k = k
        best_c = c
choice = [str(kayaks[i][0]) for i in range(best_k)] + [str(catamarans[i][0]) for i in range(best_c)]
print(optimal)
print(' '.join(choice))