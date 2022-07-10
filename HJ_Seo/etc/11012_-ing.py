# from sys import stdin

# def getnum(x1,x2,y1,y2,lst):
#     cnt = 0
#     lst = filter(lambda x: x[0] >= x1 and x[0]<=x2,lst)
#     lst = set(filter(lambda x: x[1] >= y1 and x[1]<=y2,lst))
#     return len(lst)

# case = int(input())

# for i in range(case):
#     cnt = 0
#     n,m = map(int,stdin.readline().strip().split())
    
#     dots = {tuple(map(int,stdin.readline().strip().split())) for _ in range(n)} # O(n + log(n))
    
#     while m != 0:
#         m -= 1
#         x1,x2,y1,y2 = map(int,stdin.readline().strip().split())
#         cnt += getnum(x1,x2,y1,y2,dots)
#         # O(n) for each.
        
#     print(cnt)
    
# O(n*m) alg.
# ! initial code.

from sys import stdin

def count_leng(lst,y1,y2):
    return len(tuple(filter(lambda x : x>=y1 and x<=y2,lst)))

def create_seg_tree(x,y,start,end):
    if x < start or end < x:
        return    
    else:
        segtree[x].append(y)
        create_seg_tree(2*x,y,start,(start+end)//2)
        create_seg_tree(2*x+1,y,(start+end)//2+1,end)
        return

case = int(input())

for _ in range(case):
    segtree = [[]]*131072
    n,m =map(int,stdin.readline().strip().split())
    
    for i in range(n):
        
    

