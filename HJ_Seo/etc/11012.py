from sys import stdin

def getnum(x1,x2,y1,y2,lst):
    cnt = 0
    lst = filter(lambda x: x[0] >= x1 and x[0]<=x2,lst)
    lst = set(filter(lambda x: x[1] >= y1 and x[1]<=y2,lst))
    return len(lst)

case = int(input())

for i in range(case):
    cnt = 0
    n,m = map(int,stdin.readline().strip().split())
    
    dots = {tuple(map(int,stdin.readline().strip().split())) for _ in range(n)} # O(n + log(n))
    
    while m != 0:
        m -= 1
        x1,x2,y1,y2 = map(int,stdin.readline().strip().split())
        cnt += getnum(x1,x2,y1,y2,dots)
        # O(n) for each.
        
    print(cnt)
    
# O(n*(m+1)) alg.