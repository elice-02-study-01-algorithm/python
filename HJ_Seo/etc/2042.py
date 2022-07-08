# from sys import stdin

# N,M,K = map(int,stdin.readline().strip().split())

# nums = [int(stdin.readline().strip()) for _ in range(N)]

# for _ in range(M+K):
#     a,b,c = map(int,stdin.readline().strip().split())
#     if a == 1:
#         nums[b-1] = c
#     else:
#         print(sum(nums[b-1:c]))

#! not use_segment_tree code.

from sys import stdin

N,M,K = map(int,stdin.readline().strip().split())

nums = [int(stdin.readline().strip()) for _ in range(N)]

segtree = [0]*20000000 # 6 log 10 <= 20

def inittree(idx,start,end):
    if start == end:
        segtree[idx] = nums[start]
        return segtree[idx]
    else:
        segtree[idx] = inittree(2*idx,start,(start+end)//2) + inittree(2*idx+1,(start+end)//2+1,end)
        return segtree[idx]
# inittree.. done.
inittree(1,0,N-1)

def updatetree(idx,start,end,idx2,diff):
    if idx2 < start or idx2 > end:
        # ! start와 end가 idx와 같이 움직이기 때문에 변할지 말지를 결정하는 절대적인 기준(idx2)이 필요.
        return 

    # print('change idx =',idx)
    segtree[idx] += diff
    
    if start!=end:
        updatetree(idx*2,idx2,diff,start,(start+end)//2)
        updatetree(idx*2+1,idx2,diff,(start+end)//2+1,end)
    
# update.. done.

# print(segtree[:30])

# b = 5 # idx2.. 
# diff = -3 # 5가 2로 바뀌게.
# updatetree(1,b,diff,0,N-1)

# print(segtree[:30])

def value_sum(idx,start,end,stt,ed):
    if end < stt or ed < start:
        return 0
    
    elif stt <= start and end <= ed:
        return segtree[idx]
    
    else:
        return value_sum(idx*2,start,(start+end)//2,stt,ed) + value_sum(idx*2+1,(start+end)//2+1,end,stt,ed)


# print(segtree[:20])
for _ in range(M+K):
    a,b,c = map(int,stdin.readline().strip().split())
    if a == 1:
        diff = c - nums[b-1]
        nums[b-1] = c
        updatetree(1,0,N-1,b-1,diff)
        
    else:
        print(value_sum(1,0,N-1,b-1,c-1))


'''
6 1 1
1
2
3
4
5
6

'''


'''
5 2 1
1
2
3
4
5
2 2 5
1 5 2
2 3 5
'''