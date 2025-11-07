# https://codeforces.com/problemset/problem/5/A

members = []
traffic = 0
members.append(input()[1:])
try:
    while True:
        command = input()
        if command[0] == '+':
            members.append(command[1:])
        elif command[0] == '-':
            members.remove(command[1:])
        else:
            for name in members:
                if command.startswith(name + ':'):
                    traffic += (len(command) - len(name) - 1) * len(members)
                    break
except EOFError: # Ctrl+D (on Unix/macOS) or Ctrl+Z (on Windows) signals the end of the input stream
    pass
print(traffic)