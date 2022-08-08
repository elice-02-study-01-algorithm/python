# from collections import deque

# def solution(n, roads, sources, destination):
#     answer = [-1 for _ in range(len(sources))]
#     if destination in sources:
#         answer[sources.index(destination)] = 0
    
#     check = [False for _ in range(n+1)]
#     check[destination] = True

#     Q = deque([destination])
#     leng = 1
    
#     while True:
#         before = deque()
#         used_road = []
        
#         while len(Q) != 0:
#             road = Q.popleft()

#             for i in range(len(roads)):
#                 if road in roads[i]:
#                     used_road.append(i)

#                     tmp = roads[i].copy()
#                     tmp.remove(road)
#                     tmp = tmp[0]

#                     if check[tmp] == False:
#                         before.append(tmp)
#                         check[tmp] = True

#                         if tmp in sources:
#                             answer[sources.index(tmp)] = leng
            
#         if len(before) == 0:
#             break
        
#         Q = before
#         leng += 1

#         # for i in used_road[::-1]:
#         #     del roads[i]

#     return answer

# !  시간초과. 역시 used_road를 지우는 작업으로 부담을 줄여야 할듯.

# from collections import deque

# def solution(n, roads, sources, destination):
#     answer = [-1 for _ in range(len(sources))]
#     if destination in sources:
#         answer[sources.index(destination)] = 0
    
#     check = [False for _ in range(n+1)]
#     check[destination] = True

#     Q = deque([destination])
#     leng = 1
    
#     while True:
#         before = deque()
#         used_road = set()
        
#         while len(Q) != 0:
#             road = Q.popleft()

#             for i in range(len(roads)):
#                 if road in roads[i]:
#                     if i in used_road:
#                         continue
                    
#                     used_road.add(i)

#                     tmp = roads[i].copy()
#                     tmp.remove(road)
#                     tmp = tmp[0]

#                     if check[tmp] == False:
#                         before.append(tmp)
#                         check[tmp] = True

#                         if tmp in sources:
#                             answer[sources.index(tmp)] = leng
            
#         if len(before) == 0:
#             break
        
#         Q = before
#         leng += 1
#         for i in list(used_road)[::-1]:
#             del roads[i]

#     return answer

# ! 런타임애러??..

# from collections import deque

# def solution(n, roads, sources, destination):
#     answer = [-1 for _ in range(len(sources))]
#     if destination in sources:
#         answer[sources.index(destination)] = 0
    
#     check = [False for _ in range(n+1)]
#     check[destination] = True

#     Q = deque([destination])
#     leng = 1
    
#     while True:
#         before = deque()
#         used_road = []
        
#         while len(Q) != 0:
#             road = Q.popleft()

#             for i in range(len(roads)):
#                 if road in roads[i]:
#                     if i not in used_road:
#                         used_road.append(i)

#                     tmp = roads[i].copy()
#                     tmp.remove(road)
#                     tmp = tmp[0]

#                     if check[tmp] == False:
#                         before.append(tmp)
#                         check[tmp] = True

#                         if tmp in sources:
#                             answer[sources.index(tmp)] = leng
            
#         if len(before) == 0:
#             break
#         print(before)
#         Q = before
#         leng += 1
#         for i in sorted(used_road,reverse=True):
#             del roads[i]
#         print(roads)
#     return answer

# ! 첫 번째보다 시간이 더걸리네,,?,,,

# from collections import deque

# def solution(n, roads, sources, destination):
#     answer = [-1 for _ in range(len(sources))]
#     if destination in sources:
#         answer[sources.index(destination)] = 0
    
#     check = [False for _ in range(n+1)]
#     check[destination] = True

#     Q = deque([destination])
#     leng = 1
    
#     def pick_others(lst,current):
#         return lst[(1+lst.index(current))%2]
    
#     while True:
#         before = deque()
        
#         while len(Q) != 0:
#             road = Q.popleft()

#             for i in range(len(roads)):
#                 if road in roads[i]:

#                     tmp = roads[i].copy()
#                     tmp = pick_others(tmp,road)

#                     if check[tmp] == False:
#                         before.append(tmp)
#                         check[tmp] = True

#                         if tmp in sources:
#                             answer[sources.index(tmp)] = leng
            
#         if len(before) == 0:
#             break
        
#         Q = before
#         leng += 1
        
#     return answer

# ! roads list를 재구성하는 과정에서 과한 시간이 뺏김.. used_road는 안쓰는게 낮다.


# ~~~~~~~


# ! 시간이 안줄어드네..?... 점수 그대로.

# def solution(n, roads, sources, destination):
#     answer = [] 
    
#     dist = [-1 for _ in range(n+1)]
#     dist[destination] = 0
#     check_roads = {i for i in range(len(roads))}
#     leng = 1
    
    
#     while len(check_roads) != 0:
#         used_roads = set()
#         before = set()
#         for i in check_roads:
#             if dist[roads[i][0]] != -1 and dist[roads[i][1]] != -1: # 양쪽 다 거리가 이미 정해진 길이므로.
#                 used_roads.add(i)
                
#             elif dist[roads[i][0]] != -1:
#                 before.add(roads[i][1])
#                 used_roads.add(i)
            
#             elif dist[roads[i][1]] != -1:
#                 before.add(roads[i][0])
#                 used_roads.add(i)
        
#         # print(before)
#         for i in before:
#             dist[i] = leng
        
#         # print(used_roads)
#         check_roads -= used_roads
#         leng += 1
    
#     for i in sources:
#         answer.append(dist[i])
    
#     return answer

# ! 마지막 case 제외 통과... 아마 path 형식으로 되있는 worst case같은데 더 좋은 방법이 뭐가 있을까..

def solution(n, roads, sources, destination):
    answer = [-1 for _ in range(len(sources))] 
    if destination in sources:
        answer[sources.index(destination)] = 0

    dist = [-1 for _ in range(n+1)]
    dist[destination] = 0
    check_roads = {i for i in range(len(roads))}
    leng = 1
    
    while len(check_roads) != 0:
        used_roads = set()
        before = set()
        for i in check_roads:
            if dist[roads[i][0]] != -1 and dist[roads[i][1]] != -1: # 양쪽 다 거리가 이미 정해진 길이므로.
                used_roads.add(i)
                
            elif dist[roads[i][0]] != -1:
                before.add(roads[i][1])
                used_roads.add(i)
            
            elif dist[roads[i][1]] != -1:
                before.add(roads[i][0])
                used_roads.add(i)
        
        for i in before:
            dist[i] = leng
            if i in sources:
                answer[sources.index(i)] = leng
        
        check_roads -= used_roads
        leng += 1

        if len(used_roads) == 0 or answer.count(-1) == 0:
            break
    
    if answer.count(-1) != 0:
        for i in sources:
            answer[sources.index(i)] = dist[i]
    
    return answer

# !!!!!! 아몰랑!!!!!!!!!!!!!!!!!!!!! 마지막 케이스 제외 통과.

# n = 5 # 3
# roads = [[1, 2], [1, 4], [2, 5], [2, 4], [4, 5]] # [[1,2],[2,3]]
# sources = [1,3,5] # [2,3]
# destination = 5 # 1

# print(solution(n, roads, sources, destination))