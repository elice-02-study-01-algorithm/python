from sys import stdin
input = stdin.readline

people = int(input())
time = list(map(int, input().split()))
minTime = 0
time.sort()

for i in range(people):
    for j in range(i+1):
        minTime += time[j]

print(minTime)
