nums = [1,2,3,4,5,6,7,8,9,10]
segtree = [0] * 100 # nums의 크기에 따라 segtree의 크기도 커져야하지만 여기선 100으로도 충분하다.
N = len(nums)

def inittree(idx,start,end):
    if start == end:
        segtree[idx] = nums[start]
        return segtree[idx]
    else:
        segtree[idx] = inittree(2*idx,start,(start+end)//2) + inittree(2*idx+1,(start+end)//2+1,end)
        return segtree[idx]
    
inittree(1,0,N-1)

print(segtree[:30])