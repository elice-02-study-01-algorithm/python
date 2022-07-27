import sys

s1 = list(sys.stdin.readline().rstrip())
s2 = []

m = int(sys.stdin.readline())

for _ in range(m):
    command = list(map(str, sys.stdin.readline().rstrip().split()))
    if command[0] == 'L':
        if s1:
            s2.append(s1.pop())
    elif command[0] == 'D':
        if s2:
            s1.append(s2.pop())
    elif command[0] == 'B':
        if s1:
            s1.pop()
    # P $
    else:
        s1.append(command[1])
        
s1 = s1 + list(reversed(s2))
result = ""
for word in s1:
    result += word
print(result)