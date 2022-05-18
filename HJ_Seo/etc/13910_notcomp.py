'''
만들어질 수 없는 케이스는?
1. (초기) N < wicks[0]
2. ex) 5 2 \n 3 4 같은 케이스..  1997 2 \n 999 996 같은 케이스...
--> ???????????????????????????????????????????????????????
3. ex) 1999 3 \n 999 997 996

M >= 3이고, 각 윅의 크기가 다른 경우..?..
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Does exist (x1, ... , x_M) in Z^M s.t. sigma x_i * wicks[i] = N, and if it exist, what is the possible of the nimimum of max([x1, ... , x_M])?.


'''
def mulsum(wicks,cnt,M):
    return sum([wicks[i]*cnt[i] for i in range(M)])

N,M = map(int,input().strip().split())
wicks = list(map(int,input().strip().split()))

wick_set = set(wicks)
wick_num = []
for i in wick_set:
    wick_num.append(wicks.count(i))



# maxi = N//wicks[-1] + 1
# cnt = [maxi]*M

# poss_nbr = set()

# while cnt != [0]*M:
#     if mulsum(wicks,cnt,M) == N:
#         poss_nbr.add(max(mulsum(wicks,cnt,M)))  #100개의 1이 있을때는?... 10000만 되도 10000**100..,,,,
    

# if len(poss_nbr) == 0:
#     print(-1)
# else:
#     print(min(poss_nbr))

