from sys import stdin
input = stdin.readline

N = int(input())
sequence = list(map(int, input().split()))

maxlength = [1 for _ in range(N)]
minlength = [1 for _ in range(N)]
for i in range(1, len(sequence)):
    if sequence[i-1] <= sequence[i]:
        maxlength[i] = max(maxlength[i-1] + 1, maxlength[i])
    if sequence[i-1] >= sequence[i]:
        minlength[i] = max(minlength[i-1] + 1, minlength[i])

print(max(max(maxlength), max(minlength)))