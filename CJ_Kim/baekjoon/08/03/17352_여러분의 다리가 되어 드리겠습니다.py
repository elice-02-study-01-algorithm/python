# union find 시간 초과
'''
import sys
input = sys.stdin.readline

islandNum = int(input())

class DisjointSet:
    def __init__(self, n):
        self.data = [-1 for _ in range(n)]
        self.size = n

    def upward(self, change_list, index):
        value = self.data[index]
        if value < 0:
            return index
    
        change_list.append(index)
        return self.upward(change_list, value)

    def find(self, index):
        change_list = []
        result = self.upward(change_list, index)

        # 여기서 시간 초과가 났을 것
        for i in change_list:
            self.data[i] = result

        return result

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return 

        if self.data[x] < self.data[y]:
            self.data[y] = x
        elif self.data[x] > self.data[y]:
            self.data[x] = y
        else:
            self.data[x] -= 1
            self.data[y] = x
        self.size -= 1

islandSet = DisjointSet(islandNum+1)

for _ in range(islandNum-2):
    island01, island02 = map(int, input().strip().split())
    
    islandSet.union(island01, island02)

# print(islandSet.data)
'''
# 5
# 1 2
# 2 3
# 4 5
# [-1, -2, 1, 1, -2, 4]
'''
rootIsland = []
for i in range(1, islandNum+1):
    if list(islandSet.data)[i] < 0:
        rootIsland.append(i)
    if len(rootIsland) == 2:
        break

print(*rootIsland)
'''

# class 안 쓴 union find - 틀렸습니다.


# 왜 틀렸는지 잘 모르겠습니다... 
# 아직 파보고는 있는데 혹시 코드리뷰 해주시는 분께서 찾으신다면 알려주세요!
# 꼭 찾아달라는 것은 아니고 추측도 환영입니다!

import sys
input = sys.stdin.readline

islandNum = int(input())

mapInfo = [[] for _ in range(islandNum-2)]
visitedIsland = [0 for _ in range(islandNum+1)]

# root가 되는 것들은 음수이기 때문에 음수가 되는 것들을 root로 뽑아내기
def find(a):
    if visitedIsland[a] > 0:
        return visitedIsland[a]
    return a

# def find(a):
#     if visitedIsland[a] <= 0:
#         return a
    
#     return find(visitedIsland[a])

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    # root가 같으면 같은 root 할당하기
    if root_a == root_b:
        visitedIsland[a] = root_a
        visitedIsland[b] = root_b
        return
    
    # 본인이 각각 루트면 둘 중 작은 걸로 root만들어주기
    if root_a == a and root_b == b:
        visitedIsland[a] -= 1
        visitedIsland[b] = a
        return
    
    # 둘 중 작은 root를 가진 것으로 root 가리키기
    elif root_a < root_b:
        visitedIsland[b] = root_a
        return
    elif root_a > root_b:
        visitedIsland[a] = root_b
        return

# 받을 때마다 root 만들고 가리켜주기
for i in range(islandNum-2):
    island01, island02 = sorted(map(int, input().strip().split()))
    union(island01, island02)

answer = []
# root인 것들 모아주는데, 1은 무조건 넣어주고 1에 포함되지 않은 root 넣어주기
for i in range(1, len(visitedIsland)):
    if -1 <= visitedIsland[i] <= 0:
        answer.append(i)

if 1 not in answer:
    answer.append(1)
print(*answer)

