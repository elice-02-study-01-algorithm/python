from sys import stdin

dpa = [[0 for _ in range(15)] for _ in range(15)]
dpa[0] = [i for i in range(15)]

for i in range(1,15):
    for j in range(1,16):
        dpa[i][j-1] = sum(dpa[i-1][:j])
        
# for i in dpa:
#     print(i)

m = int(stdin.readline().strip())
if m == 0:
    exit(0)

for i in range(m): #k층 n호.
    k = int(stdin.readline().strip())
    n = int(stdin.readline().strip())  
    print(dpa[k][n])