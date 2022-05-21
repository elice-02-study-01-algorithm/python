from sys import stdin

n = int(stdin.readline())

for _ in range(n):
    arr = stdin.readline().strip()
    stack = 0
    done = 0
    for i in arr:
        if i == '(':
            stack += 1
        else:
            stack -= 1
        
        if stack == -1:
            print('NO')
            done = 1
            break
    
    if done == 0:
        if stack == 0:
            print("YES")
        else:
            print("NO")