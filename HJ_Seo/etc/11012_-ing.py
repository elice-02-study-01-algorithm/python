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

def count_dots(x1,x2,y1,y2,start,end):
    if x2<start or end<x1:
        return 0
    elif x1 <= start and end <= x2:
        return count_leng(1111111111111111111111,y1,y2) # start와 end로부터 index를 뽑는 방법은?
    else:
        return 1
case = int(input())

for _ in range(case):
    coordinates = [[] for _ in range(65537)]
    n,m =map(int,stdin.readline().strip().split())
    
    for i in range(n):
        x,y = map(int,stdin.readline().strip().split())
        coordinates[x].append(y)
    print(coordinates[:10])
    
    segtree = [[] for _ in range(65537)] + coordinates
    
    x = 65536
    # ! make_seg_tree는 coordinates가 다 들어간 이후 만들어야 한다!! (같이 만들게 된다면 메모리 누수가 굉장할듯..)
    while x != 0:
        segtree[x] = segtree[2*x+1] + segtree[2*x]
        x -= 1


    print(segtree[:30])
    

'''
1   
3 1
3 5
2 3
1 1
'''
