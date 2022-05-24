from sys import stdin
input = stdin.readline

# 666, 1666, 2666 ...6660, 6666 ... 9666, 10666. 11666 ... 16666, 16667
N = int(input())
title = 666
count = 0
while True:
    if "666" in str(title):
        count += 1
        if count == N:
            print(title)
            break
    title += 1