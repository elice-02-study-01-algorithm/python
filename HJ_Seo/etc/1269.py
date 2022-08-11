from sys import stdin

XXX = stdin.readline()

A = set(map(int,stdin.readline().strip().split()))
B = set(map(int,stdin.readline().strip().split()))

print(len(A^B))