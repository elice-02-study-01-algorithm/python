# N명의 플레이어끼리 화살표 게임, 한 사람을 선택하여 벌칙을 줌
# 처음에 한 사람을 술래로 정함
# 더게임오브데쓰..?
# N명의 사람들은 왼손과 오른손으로 한 명씩 지목(같은 사람 불가능)
# 술래부터 시작해서 한명씩 오른손이나 왼쪽으로 지목한 사람이 술래가 됨
# 처음 술래가 지정한 P번째에 걸린 사람이 벌칙
# P가 몇이든 절대 술래로 지목되지 않을 사람의 수를 출력
# bfs

from sys import stdin
inputs = stdin.readline

people, starter = map(int, inputs().split())
theGameOfDeath = [tuple(map(int, inputs().split())) for _ in range(people)]

tagger = [starter]
visit = [0 for _ in range(people+1)]
visit[starter] = 1
for person in tagger:
    left, right = theGameOfDeath[person-1]
    if not visit[left]:
        visit[left] = 1
        tagger.append(left)
    if not visit[right]:
        visit[right] = 1
        tagger.append(right)

# print(visit)
print(visit.count(0) - 1)