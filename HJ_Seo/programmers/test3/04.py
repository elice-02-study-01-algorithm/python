# def solution(n, lighthouse):
#     if n < 3:
#         return 1
    
#     conn = dict()
#     for i in lighthouse:
#         if i[0] not in conn:
#             conn[i[0]] = [i[1]]
#         else:
#             conn[i[0]].append(i[1])
        
#         if i[1] not in conn:
#             conn[i[1]] = [i[0]]
#         else:
#             conn[i[1]].append(i[0])
        
#     color_lighthouse = [False]*(n+1)
#     red = {1}
#     blue = set()
#     color_lighthouse[1] = True
#     check = {1}
#     red_blue = 1


#     while True:
#         tmp = set()
#         for i in check:
#             for j in conn[i]:
#                 if color_lighthouse[j] == False:
#                     color_lighthouse[j] = True
#                     tmp.add(j)
        
#         if len(tmp) == 0:
#             return min(len(red),len(blue))

#         if red_blue == 1:
#             blue.update(tmp)
#             red_blue = 0
#         else:
#             red.update(tmp)
#             red_blue = 1
        
#         check = tmp

# ! 문제를 착각해서 잘못 구한 red & blue 똑딱이..

# from itertools import combinations

# def solution(n, lighthouse):
#     if n < 3:
#         return 1
    
#     conn = dict()
#     for i in lighthouse:
#         if i[0] not in conn:
#             conn[i[0]] = {i[0],i[1]}
#         else:
#             conn[i[0]].add(i[1])
        
#         if i[1] not in conn:
#             conn[i[1]] = {i[1],i[0]}
#         else:
#             conn[i[1]].add(i[0])
#     lighthouse_set = {i for i in range(1,n+1)}

#     for i in range(3,n//2):
#         for j in combinations(lighthouse_set,i):
#             tmp = set()
#             for k in j:
#                 tmp.update(conn[k])

#             if len(tmp) == n:
#                 return i

#     return n//2

# ! 개무식하게 try.. n의 최댓값이 10만인 시점에서 실행하면 안됨.

def solution(n, lighthouse):
    if n < 3:
        return 1
    lights = [0] * (n+1)
    need = [False] * (n+1)
    conn = dict()
    for i in lighthouse:
        lights[i[0]] += 1
        lights[i[1]] += 1

        if i[0] not in conn:
            conn[i[0]] = {i[0],i[1]}
        else:
            conn[i[0]].add(i[1])
        
        if i[1] not in conn:
            conn[i[1]] = {i[1],i[0]}
        else:
            conn[i[1]].add(i[0])

    # print(lights)

    def in_light(num):
        for i in conn[num]:
            if need[i] == True:
                return False
        
        need[num] = True
        return True

    tmp = [0]*(n+1)
    for i in lighthouse:
        if lights[i[0]] == 1 or lights[i[1]]:
            if lights[i[0]] == 1:
                need[i[1]] = True
                tmp[i[1]] += -1
            elif lights[i[1]] == 1:
                need[i[0]] = True
                tmp[i[0]] += -1
    
    for i in range(1,n+1):
        lights[i] += tmp[i]

    print(lights)
    print(need)

    # ! 여기 다음을 수정하면 맞을텐데.. 아이디어를 모르겠네..,,

    for i in range(1,n+1):
        if need[i] == False:
            in_light(i)   # ! 이렇게 하면 과한 커버가 만들어지는데...

    return need.count(True)

    # result = 0
    # while True:
    #     maxi = lights.index(max(lights))
    #     if maxi <= 0:
    #         return result

    #     result += 1
    #     lights[maxi] = 0
    #     for i in conn[maxi]:
    #         lights[i] -= 1