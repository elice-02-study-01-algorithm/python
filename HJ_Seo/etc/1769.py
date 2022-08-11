'''
after one step, num <= 9000000.. 
8999999
62
8
'''

import re
from sys import stdin
# import time

num = re.sub('0','',stdin.readline().strip())

def cnt_change_num(num):
    cnt = 0
    while True:
        if len(num) == 1:
            print(cnt)
            print("YES") if num in ['3','6','9'] else print("NO")
            return
        
        cnt += 1
        tmp = 0
        tmp2 = 0
        for i in range(1,10):
            x = num.count(str(i))
            tmp += i*x
            tmp2 += x
            if tmp2 == len(num):
                break
        
        num = str(tmp)

cnt_change_num(num)

# ! 1번. done.. 한큐에 성공.. 그런데 왜 이게 정답률이 30%이지..?;;

# def cnt_change_num2(num):
#     cnt = 0
#     while True:
#         if len(num) == 1:
#             print(cnt)
#             print("YES") if num in ['3','6','9'] else print("NO")
#             return
        
#         cnt += 1
#         tmp = 0
#         for i in num:
#             tmp += int(i)
        
#         num = str(tmp)

# # ! 2번. 

# stt_time = time.time()
# cnt_change_num(num)
# print(time.time()-stt_time)

# stt_time = time.time()
# cnt_change_num2(num)
# print(time.time()-stt_time)