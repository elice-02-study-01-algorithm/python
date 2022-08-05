# https://www.acmicpc.net/problem/1094

stick = 64

n = int(input())
piece = []

while n != 0:
    if stick<=n:
        piece.append(stick)
        n -= stick
    
    stick = stick//2

print(len(piece))

