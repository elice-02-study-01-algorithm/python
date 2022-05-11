# 마크문제
from sys import stdin

N,M,B = map(int,input().strip().split())

ground = []
for i in range(N):
    ground += list(map(int,stdin.readline().strip().split()))
# 땅의 모양이 일렬이든 아니든 계산에는 상관이 없기 때문.


#! 아마 아래꺼를 수정해야 할 가능성이 높다. 블럭을 깰 때의 시간이 블록을 만들 때보다 더 길기 때문.  B를 조정해줘야하나??...
sum_ground = sum(ground)
totalbound = N*M

aim_height = sum_ground//totalbound + 1
# 첫 땅의 평균 높이(기준) ---  땅을 최소로 깨기 위함.

## 게산의 영역.
need_block = aim_height*totalbound - sum_ground

while need_block > B:
    if aim_height == 0:
        break
    
    aim_height -= 1 
    need_block = aim_height*totalbound - sum_ground
#두번째 출력값 aim_height.    

time = 0
for i in ground:
    time += (aim_height-i) if i < aim_height else 2*(i-aim_height)
#첫 번째 출력값 time.

print(time,aim_height)