from sys import setrecursionlimit
setrecursionlimit(10**6)

def after(start,end):
    if start > end:
        return
    
    root = pre[start]
    
    if pre[-1] < root:
        after(start+1,end)
        print(root)
        return
    
    mid = end+1
    for i in range(start+1,end+1):
        if pre[i]>root:
            mid = i
            break
    
    after(start+1,mid-1)
    after(mid,end)
    print(root)
    return

pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break

after(0,len(pre)-1)

# ! 1. index 설정은 항상 조심..!... range의 end... end + 1.
# !! 2. 효과적인 풀이를 본 후 개선 : index를 쓰는 것도 좋지만 많이 비교할 수 밖에 없는 것은 변수로 넣어주면 시간 관리에 훨씬 효과적이다.