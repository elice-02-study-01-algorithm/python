# def solution(board, skill):
#     for i in skill:
#         if i[0] == 1:
#             for j in range(i[1],i[3]+1):
#                 for k in range(i[2],i[4]+1):
#                     board[j][k] -= i[5]
#         if i[0] == 2:
#             for j in range(i[1],i[3]+1):
#                 for k in range(i[2],i[4]+1):
#                     board[j][k] += i[5]
                    
#     cnt = 0
#     for i in sum(board,[]):
#         if i > 0:
#             cnt += 1
#     return cnt

# # ! first.. fail.

# import numpy as np

# def solution(board, skill):
#     board = np.array(board)
#     for i in skill:
#         if i[0] == 1:
#             board[i[1]:i[3]+1,i[2]:i[4]+1] -= i[5]
#             # for j in range(i[1],i[3]+1):
#             #     for k in range(i[2],i[4]+1):
#             #         board[j][k] -= i[5]
#         if i[0] == 2:
#             board[i[1]:i[3]+1,i[2]:i[4]+1] += i[5]
#             # for j in range(i[1],i[3]+1):
#             #     for k in range(i[2],i[4]+1):
#             #         board[j][k] += i[5]
    
#     cnt = 0 # 기껏해야 1만번 실행.. 건들필요 없음.
#     for i in board:
#         for j in i:
#             if j > 0:
#                 cnt += 1
#     # cnt = 0
#     # for i in sum(board,[]):
#     #     if i > 0:
#     #         cnt += 1 
#     return cnt
    
# ! second.. fail..!..

# 참고글 : https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/

import numpy as np
    
def solution(board, skill):

    n = len(board[0]) # row
    m = len(board) # col
    board = np.array(board)
    
    onboard = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in skill:
        if i[0] == 1:
            onboard[i[1]][i[2]] -= i[5]
            onboard[i[1]][i[4]+1] += i[5]
            onboard[i[3]+1][i[2]] += i[5]
            onboard[i[3]+1][i[4]+1] -= i[5]

        if i[0] == 2:
            onboard[i[1]][i[2]] += i[5]
            onboard[i[1]][i[4]+1] -= i[5]
            onboard[i[3]+1][i[2]] -= i[5]
            onboard[i[3]+1][i[4]+1] += i[5]
    
    onboard = np.array(onboard)
    
    for i in range(m):
        onboard[i+1] += onboard[i]
        
        for j in range(n):
            onboard[i][j+1] += onboard[i][j]
    
    board += onboard[0:m,0:n]
    
    cnt = 0 
    for i in board:
        for j in i:
            if j > 0:
                cnt += 1
                
    return cnt
    
# last.. clear.. 누적합이라는 좋은 방법을 알 수 있는 기회였다!