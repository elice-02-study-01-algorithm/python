from sys import stdin

N, K = map(int, stdin.readline().split())

table = [x for x in range(1, N + 1)]
Josephus = []
idx = 0

while table:
    idx = (idx + K - 1) % len(table)
    Josephus.append(table.pop(idx))

# print('<' + str(Josephus).strip("[]") + '>')
print('<' + ', '.join(map(str, Josephus)) + '>')
