# https://codeforces.com/problemset/problem/4/D
 
def fit(envelope1, envelope2):
    return envelope1['width'] < envelope2['width'] and envelope1['height'] < envelope2['height']
 
n,card_w,card_h = [int(x) for x in input().split()]
envelopes = []
for i in range(n):
    width, height = [int(x) for x in input().split()]
    if width > card_w and height > card_h:
        envelopes.append({'width': width, 'height': height, 'index': i+1})
 
if not envelopes:
    print(0)
else:
    list = sorted(envelopes, key = lambda x: x['width'])
    n = len(list)
    longest_chain = [1] * n
    parent = [-1] * n
    max_chain = 1
    outer_index = 0
    for i in range(n): # for envelope1 in list
        for j in range(i): # for envelope2 in list
            if fit(list[j], list[i]) and longest_chain[j] + 1 >longest_chain[i]: # if fits and contain longer chain
                longest_chain[i] = longest_chain[j] + 1
                parent[i] = j
                if longest_chain[i] > max_chain:
                    max_chain = longest_chain[i]
                    outer_index = i

    layers_reversed = []
    current = outer_index
    while current != -1: # backtrack
        layers_reversed.append(str(list[current]['index']))
        current = parent[current]
    print(max_chain)
    print(' '.join(layers_reversed[::-1]))