import math
import heapq
from sys import stdin
input = stdin.readline

n = int(input())
a_list = list(map(int, input().split()))
m = int(input())

# [ 세그먼트 트리 초기화 ]
# tree 배열의 크기: 2^(log(n)+1)-1
# tree = [0] * (pow(2,math.ceil(math.log(len(a_list),2))+1))-1
# 나는 그냥 넉넉하게 len(a_list)*4
# 트리에는 주어진 수열이 들어가는 것이 아니라 인덱스를 넣는다.
# start : 배열의 시작 인덱스, end : 배열의 마지막 인덱스

tree = [0] * (len(a_list) * 4)
node = 1
def init(start, end):
    mid = (start+end) // 2
    if start == end:
        tree[node-1] = start
    else:
        init(start, mid)
        init(mid+1, end)

        if a_list[tree[node*2-1]] < a_list[tree[node*2]]:
            tree[node-1] = tree[node*2-1]
        else:
            tree[node-1] = tree[node*2]

# [ 값 업데이트 ]
# 값이 업데이트 되면 다시 초기화 
# def update(start, end):

for i in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:
        idx = query[1] - 1
        a_list[idx] = query[2]
        init(0, n)
    else:
        print(tree[node-1])