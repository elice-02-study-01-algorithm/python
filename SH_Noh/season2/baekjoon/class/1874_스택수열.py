from sys import stdin
input = stdin.readline

n = int(input())
stack = []
answer = []
cur = 1

for i in range(n):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        answer.append("+")
        cur += 1

    if num == stack[-1]:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        exit()

print(*answer, sep = "\n")