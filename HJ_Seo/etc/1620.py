from sys import stdin

N,M = map(int,stdin.readline().strip().split())
pok_dict = dict()
for i in range(1,N+1):
    x = stdin.readline().strip()
    pok_dict[str(i)] = x
    pok_dict[x] = i

while M != 0:
    print(pok_dict[stdin.readline().strip()])
        
    M -= 1
