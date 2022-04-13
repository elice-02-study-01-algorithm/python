def main():
    time,money = map(int,input().strip().split())
    
    menu_taste = []
    used_money = 0
    total_taste = 0
    
    for i in range(time):
        a,b = map(int,input().strip().split())
        if a>=b:
            total_taste += a
            used_money += 1000  #확실한건 미리 제껴놓기.
        else:
            menu_taste.append([a,b,b-a])
    
    menu_taste = sorted(menu_taste,key = lambda x: [-x[2]])  
    #먼저 선택할 기준 정하기.. 여기가 문제.. 아래쪽은 순서대로 pop을 시켜주는 곳이라 수정할 필요는 아마도? 없는데.. b-a가 항상 양수이기 때문에 이거를 추가변수로 두고 3을 먹을 수 있는 횟수가 몇번인지 필요.. 3a와 b를 비교하는게 아닌 것 같다..
    res_money = money-used_money
    can_3 = min( (res_money//1000 - len(menu_taste))//2, len(menu_taste) )
    

#     print('=======')
    
#     print('남은돈 =',money-used_money)
#     print('남은 선택지 =',menu_taste)
#     print('3천원짜리를 선택할 수 있는 횟수 =',can_3)
#     print('현재 얻은 양 =',total_taste)
    
#     print('=======')
    
    while can_3 != 0:
        select_time = menu_taste.pop(0)
        # print('select_time =', select_time)
        total_taste += select_time[1]
        can_3 -= 1
    
    while len(menu_taste) != 0:
        only_select = menu_taste.pop(0)
        # print('only_select =',only_select)
        total_taste += only_select[0]
    
    # for i in range(len(menu_taste)):
    #     res_money = money-used_money
    #     select_time = menu_taste.pop(0)
    #     # print('select_time =',select_time)
    #     # print('지금까지 총량 =',total_taste)
    #     if res_money-3000 >= max(len(menu_taste)*1000,0):
    #         # print(res_money,'//',len(menu_taste)*1000)
    #         used_money += 3000
    #         total_taste += select_time[1]
    #     else:
    #         used_money += 1000
    #         total_taste += select_time[0]
    
#     print('=======모두 선택한 결과===========')
    
#     print('남은돈 =',money-used_money)
#     print('남은 선택 =',menu_taste)
#     print('결과로 얻은 양 =',total_taste)
    
#     print('=======')
    
    return print(total_taste)
    
    
if __name__=="__main__":
    main()
############################## 내꺼 맞음.

# import sys

# def input():
#     return sys.stdin.readline().rstrip()
    
# N, K = map(int, input().split())
# data = []
# visited = [0] * (N + 1)
# cnt_3 = (K // 1000 - N) // 2
# answer = 0
# # print('cnt_3 =',cnt_3)
# for i in range(N):
#     a, b = map(int, input().split())
#     data.append((a, i, 0))
#     data.append((b, i, 1))
    
# data.sort(reverse=True)  #여기서 실수가 있나?
# print('data =', data)
# for dt in data:
#     if visited[dt[1]]:
#         print('계산에서 뺌1 : ',dt)
#         continue
#     if dt[2]:
#         if not cnt_3:
#             print('계산에서 뺌2 : ',dt)
#             continue
#         cnt_3 -= 1
        
#     answer += dt[0]
#     print('더해진거 =',dt)
#     visited[dt[1]] = 1
    
# print(answer)





############################ 답지 틀림.
'''
3 7000
5 30
6 20
7 20

wanted result : 57
do result : 56
'''

# import sys

# def input():
#     return sys.stdin.readline().rstrip()
    
# N, K = map(int, input().split())
# data = []
# visited = [0] * (N + 1)
# cnt_3 = (K // 1000 - N) // 2
# answer = 0

# for i in range(N):
#     a, b = map(int, input().split())
#     data.append((a, i, 0))
#     data.append((b, i, 1))
    
# data.sort(reverse=True)

# for dt in data:
#     if visited[dt[1]]:
#         continue
#     if dt[2]:
#         if not cnt_3:
#             continue
#         cnt_3 -= 1
        
#     answer += dt[0]
#     visited[dt[1]] = 1
    
# print(answer)



