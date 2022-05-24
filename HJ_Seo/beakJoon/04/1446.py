from sys import stdin

n, rang = map(int,stdin.readline().strip().split()) #지금길의 갯수, 길이. 0<= n <=12, 0<= rang <= 10000

roads = {}
for _ in range(n):
    a,b,c = map(int,stdin.readline().strip().split()) #a < b.
    if b > rang: #목표지점을 지나면 빠꾸가 안됨.
        continue 
    
    if b - a > c: #지름길의 길이가 원래보다 길어도 pass.
        if (a,b) not in roads:
            roads[(a,b)] = c
        else:
            roads[(a,b)] = min(roads[(a,b)],c) #지름길의 시/종점이 같은게 있으면 짧은거 pick.

road = [_ for _ in range(rang+1)]
road[1] = 1
for i in range(2,rang+1):
    for j in roads:
        if j[1] == i:
            # print(j)
            road[i] = min(road[i],road[j[0]]+roads[j])
            # print(road[i])
    
    road[i] = min(road[i],road[i-1] + 1)

print(road[-1])
# done.



# ! 시간 초과..!.. 케이스가 많으면 오래걸리나보다..,,,
# pick_roads = sorted([[i] for i in roads])
# roads_lst = sorted([i for i in roads])

# temp = 0
# while True:
#     if temp == []:
#         break
    
#     temp = []
#     len_picks = len(pick_roads)
#     for i in range(len_picks):
#         for j in range(len(roads_lst)):
#             if pick_roads[i]+[roads_lst[j]] not in pick_roads and pick_roads[i][-1][1] <= roads_lst[j][0]:
#                 temp.append(pick_roads[i]+[roads_lst[j]])

#     pick_roads += temp


# rang_result = rang
# # print(roads)
# # print(pick_roads[-1])
# for i in pick_roads:
#     temp = rang
#     for j in i:
#         temp += roads[j] # i에 있는 각각의 j에 대해 + 지금길의 길이 - 원래 길의 길이
#     print(temp)
#     rang_result = min(rang_result,temp)
    
# print(rang_result)