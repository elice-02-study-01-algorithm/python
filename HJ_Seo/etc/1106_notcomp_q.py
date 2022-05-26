from sys import stdin

C,N = map(int,stdin.readline().strip().split()) #aim_num, num_of_city

lst= []
for i in range(N):
    lst.append(tuple(map(int,stdin.readline().strip().split()))) # price,get_num

lst = sorted(lst, key = lambda x: -x[1]/x[0])

# print(lst)

del_set = set()
for i in range(N-1):
    for j in range(i+1,N):
        if lst[i][0]<=lst[j][0] and lst[j][1]<=lst[i][1]:
            del_set.add(j) #극단적인 비효율 cut.

for i in list(del_set)[::-1]:
    del lst[i]
    
# print(lst)
result = 0
res_set = set()

for i in range(len(lst)):
    if lst[i][1]>= C:
        res_set.add(lst[i][0])

for i in range(len(lst)):
    if lst[i][1] <= C:
        x = C//lst[i][1]
        
        
            
            



# result_set = set()
# lst = []
# for i in range(N):
#     lst.append(list(map(int,stdin.readline().strip().split())))

# lst = sorted(lst,key = lambda x: -x[1]/x[0])

# cut = 0
# for i in lst:
#     if i[1] <= C:
#         x = C//i[1]
#         C = C%i[1]
#         cut += x*i[0]
#         break

# if C == 0:
#     print(cut)
#     exit(0)

# cal_dict = {0:0}
# for i in lst:
#     cal_dict[i[1]] = i[0] # key:고용인원. val:(최소)비용

# while len(cal_dict) != 0:
#     # print(cal_dict)
#     temp_dict = {}
#     for i in cal_dict.items():
#         for j in lst:
#             if i[0]+j[1]>=C:
#                 # print('result_set_input = ',i[1]+j[0])
#                 result_set.add(i[1]+j[0])
#             elif i[0]+j[1] in temp_dict.keys():
#                 temp_dict[i[0]+j[1]] = min(temp_dict[i[0]+j[1]],i[1]+j[0])
#             else:
#                 temp_dict[i[0]+j[1]] = i[1]+j[0]
#     cal_dict = temp_dict

# # print(cut,C)
# # # print(lst)
# # print(result_set)
# print(cut+min(result_set))

# ! 틀림... 왜??

# ex. 12명 필요, lst = [[11,30],[1,1]] --> 11
# ex2. 12명 필요. [[5,6],[4,4]] --> 10
# ex3. 12명 필요. [[100,300],[5,1]] --> 1*12 = 12 .. # ! 5*12 = 60
# ex4. 12명 필요. [[3,300],[5,1]] --> 300*1 > 12 .. # ! 3
# ex5. 100명 필요. [[4,9],[1,2]] --> 9*11 + 2*1 = 101 >= 100.
# ex6. 12명 필요. [[100,300],[44,15],[5,1]] --> 15 >= 12 .. 44