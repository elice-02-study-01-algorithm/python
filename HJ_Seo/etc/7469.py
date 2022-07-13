from sys import stdin

n,m = map(int,stdin.readline().strip().split())
nums = list(map(int,stdin.readline().strip().split()))
# sorted_nums = sorted(nums)

x = 1
while True:
    x*=2
    if x >= n:
        break
# print(x)
#x = the nbr of vertices of segment tree + 1?
nums = nums + [0]*(x-len(nums))
# nums = [1, 5, 2, 6, 3, 7, 4, 0] = segtree[1]
# segtree[2] = nums[0:4], segtree[3] = nums[4:8]
# print(nums[0:4],nums[4:8])
segtree = [[] for _ in range(2*x)]

def make_seg_tree(idx,start,leng):
    # print(idx,start,leng)
    if leng == 1:
        segtree[idx] = nums[start:start+1]
        return segtree[idx]
    else:
        segtree[idx] = make_seg_tree(2*idx,start,leng//2) + (make_seg_tree(2*idx+1,start + leng//2,leng//2))
        return segtree[idx]

make_seg_tree(1,0,x)

def Q(idx,start,leng,i,j):
    if leng == 0:
        return    
    elif j < start or start+leng < i:
        return 
    elif i <= start and start+leng <= j:
        union_arr.update(segtree[idx])
    else:
        Q(2*idx,start,leng//2,i,j)
        Q(2*idx+1,start+leng//2,leng//2,i,j)

while m != 0:
    
    union_arr = set()
    i,j,k = map(int,stdin.readline().strip().split())
    Q(1,0,x,i-1,j)
    for _ in range(k-1):
        union_arr.pop()
    print(union_arr.pop())
    
    m -= 1


'''
4 1
1 5 2 6

'''


'''
7 3
1 5 2 6 3 7 4
2 5 3
4 4 1
1 7 3

output : 
5
6
3
'''