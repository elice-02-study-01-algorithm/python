from sys import stdin

n = int(stdin.readline().strip())

house = [list(map(int,stdin.readline().strip().split())) for _ in range(n)]

m = 1

while m != n:
    for i in range(3):
        temp = house[m-1].copy()
        temp.pop(i)
        house[m][i] += min(temp)
    
    m += 1
    
print(min(house[-1]))

