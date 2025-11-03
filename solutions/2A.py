# https://codeforces.com/problemset/problem/2/A

rounds = int(input())
final = {}
history = [] # store history of each round winner
for i in range(rounds):
    result = input().split()
    player = result[0]
    score = int(result[1])
    history.append((player, score))
    if player in final.keys():
        final[player] += score
    else:
        final[player] = score
win = max(final.values())
candidate = [player for player, score in final.items() if score == win]
if len(candidate) == 1:
    print(candidate[0])
else:
    final = {}
    for i in range(rounds):
        if history[i][0] in candidate:
            result = history[i]
            player = result[0]
            score = int(result[1])
            if player in final.keys():
                final[player] += score
                if final[player] >= win:
                    print(player)
                    break
            else:
                final[player] = score
                if final[player] >= win:
                    print(player)
                    break