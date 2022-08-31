# from sys import stdin
# import re
# from collections import deque

# case = int(stdin.readline().strip())

# for _ in range(case):
#     switch = 1
#     orders = re.sub('RR','',stdin.readline().strip())
#     n = stdin.readline()
#     lst = stdin.readline().strip()[1:-1]
#     is_error = False
#     if len(lst) > 0:
#         arr = deque(map(str,lst.split(',')))
#     else:
#         arr = deque()
    
#     for order in orders:
#         if order == 'R':
#             switch *= -1
#         elif order == 'D':
#             if len(arr) == 0:
#                 print('error')
#                 is_error = True
#                 break
            
#             elif switch == 1:
#                 arr.popleft()
#             elif switch == -1:
#                 arr.pop()
        
#     if is_error == False:
#         if switch == 1:
#             arr = ','.join(list(arr))
#             print('['+arr+']')
#         elif switch == -1:
#             arr = ','.join(list(arr)[::-1])
#             print('['+arr+']')
        
# ! 아래는 try except로 업뎃.

from sys import stdin
import re
from collections import deque

case = int(stdin.readline().strip())

for _ in range(case):
    try:
        switch = 1
        orders = re.sub('RR','',stdin.readline().strip())
        n = stdin.readline()
        lst = stdin.readline().strip()[1:-1]
        if len(lst) > 0:
            arr = deque(map(str,lst.split(',')))
        else:
            arr = []
        
        for order in orders:
            if order == 'R':
                switch *= -1
            elif order == 'D':
                if switch == 1:
                    arr.popleft()
                elif switch == -1:
                    arr.pop()
        
        if switch == 1:
            arr = ','.join(list(arr))
            print('['+arr+']')
        elif switch == -1:
            arr = ','.join(list(arr)[::-1])
            print('['+arr+']')
    except:
        print('error')
        