# https://www.acmicpc.net/problem/11725
# ! 대강 짜가지고 업데이트 할 필요는 있어보인다... 생각나면 하겠지??

n = int(input())

tree = dict()

for _ in range(n-1):
    node1,node2 = map(int,input().split())
    if node1 not in tree:
        tree[node1] = []
    tree[node1].append(node2)
    
    if node2 not in tree:
        tree[node2] = []
    tree[node2].append(node1)
    
result = [None for _ in range(n+1)]

tmp = [(1,tree[1])]

while len(tmp) != 0:
    tmp2 = []
    for i in tmp:
        for j in i[1]:
            if result[j] == None:
                result[j] = i[0]
                tmp2.append((j,tree[j]))
    tmp = tmp2

for i in range(2,n+1):
    print(result[i])