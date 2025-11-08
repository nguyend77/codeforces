# https://codeforces.com/problemset/problem/5/C

sequence = input()
max_length = 0
count = 1
stack = [-1]

for i in range(len(sequence)):
    if sequence[i] == '(':
        stack.append(i)
    else: # sequence[i] == ')'
        if len(stack) > 1:
            stack.pop() # pair the ')' with a '('
            current_length = i - stack[-1]
            if current_length > max_length:
                max_length = current_length
                count = 1 # reset count for new max
            elif current_length == max_length:
                count += 1 # found another of the same length
        else: # every current '(' is already paired with a ')'
            stack.pop() # remove the old -1
            stack.append(i) # start new sequence

print(f'{max_length} {count}')