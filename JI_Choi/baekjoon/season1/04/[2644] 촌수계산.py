import sys


def input():
    return sys.stdin.readline().rstrip()


dict = {}
# child가 key, value가 parent인 dict 생성
for i in range(1, int(input())+1):
    dict[i] = 0

# 촌수를 구할 두 사람
child_1, child_2 = input().split()

# 부모 자식들 간의 관계의 개수만큼 for문 수행
for _ in range(int(input())):
    parent, child = map(int, input().split())
    dict[child] = parent

# 두 사람에 대한 수열을 담을 집합들 생성
set1 = {int(child_1)}
set2 = {int(child_2)}

# child_1에 대한 수열 생성
while True:
    if child_1 == 0:
        break
    child_1 = dict[int(child_1)]
    set1.add(child_1)

# child_2에 대한 수열 생성
while True:
    if child_2 == 0:
        break
    child_2 = dict[int(child_2)]
    set2.add(child_2)

# 공통 수열이 0 뿐인 경우, 친척 관계가 아님
if set1 & set2 == {0}:
    print(-1)
# 이외의 경우, 친척 관계
else:
    print(len(set1 - set2)+len(set2 - set1))
