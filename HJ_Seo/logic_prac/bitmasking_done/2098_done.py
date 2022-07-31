n = int(input())
graph = [tuple(map(int,input().strip().split())) for _ in range(n)]

visited_all = (1<<n) - 1
num = 15000001

weight_subtree = [[None]*((1<<n)-1) for _ in range(n)]

def get_min_weight(last,visited):
    if visited == visited_all:
        return graph[last][0] or num  # graph[last][0] : 마지막 고려사항. but 이게 0일 경우 num을 return하도록 함.
    
    if weight_subtree[last][visited] != None:
        return weight_subtree[last][visited]
    
    tmp = num
    for city in range(n):
        
        if visited & (1<<city) == 0 and graph[last][city] != 0:
            tmp = min(tmp, get_min_weight(city,visited | (1<<city))+graph[last][city])
    
    weight_subtree[last][visited] = tmp
    
    return tmp

print(get_min_weight(0,1))

# 주석 달아서 커밋!