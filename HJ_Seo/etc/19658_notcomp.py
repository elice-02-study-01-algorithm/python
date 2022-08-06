# https://www.acmicpc.net/problem/19658  
# ! 이거 뭔지 모르겠다.. C로 풀어야하나?

from sys import stdin,stdout
n = int(stdin.readline().strip())

diffs = tuple(map(int,stdin.readline().strip().split()))

def get_max(tup,n):
    x = 1
    lst = [x]
    for i in tup:
        tmp = lst[-1]+i
        lst.append(tmp)
        
    maxi = max(lst)
    return maxi, lst.index(maxi)

def get_init_num(tup,maxi,idx):
    num = 0
    for i in range(idx):
        num += tup[i]
    
    return maxi-num

def make_num(init_num,tup):
    lst = [init_num]
    for i in tup:
        lst.append(lst[-1]+i)
    
    return lst

maxi,idx = get_max(diffs,n)

if maxi != n:
    stdout.write('-1')
    exit(0)

init_num = get_init_num(diffs,maxi,idx)

lst = make_num(init_num,diffs)

for i in lst[:-1]:
    stdout.write(str(i))
    stdout.write(' ')
stdout.write(str(lst[-1]))

'''
x를 시작이라 하자. then, nums = [x,x+1,x+4,x+2,x+3] return 2,0 (최대 수의 idx,최소 수의 idx.)
'''