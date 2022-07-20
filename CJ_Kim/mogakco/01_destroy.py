# 효율성 테스트는 통과하지 못했습니다.

# 공격이든 회복이든 건물의 내구도가 바뀔 때 쓰는 함수
def make_change(map, r1, c1, r2, c2, degree):
    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            map[r][c] = map[r][c] + degree
    return map
    
# 내구도가 0 초과인 것들을 세는 함수
def how_many_survived(map):
    survived = 0
    for i in range(len(map)):
        for building in map[i]:
            if building > 0:
                survived += 1
    return survived


def solution(board, skill):
    building_map = board
    
    total_skill = []
    for skill_by_step in skill:
        total_skill += skill_by_step
        skill_type, r1, c1, r2, c2, degree = skill_by_step
        
        if skill_type == 1:
            degree = 0 - degree
        building_map = make_change(building_map, r1, c1, r2, c2, degree)

    answer = how_many_survived(building_map)
    return answer

ans01 = solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]) # 10

ans02 = solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]) # 6

print(ans01, ans02)