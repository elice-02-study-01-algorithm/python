def solution(board, skill):
    for i in skill:
        if i[0] == 1:
            for j in range(i[1],i[3]+1):
                for k in range(i[2],i[4]+1):
                    board[j][k] -= i[5]
        if i[0] == 2:
            for j in range(i[1],i[3]+1):
                for k in range(i[2],i[4]+1):
                    board[j][k] += i[5]
                    
    cnt = 0
    for i in sum(board,[]):
        if i > 0:
            cnt += 1
    return cnt

# ! first.. fail.

import numpy as np

def solution(board, skill):
    board = np.array(board)
    for i in skill:
        if i[0] == 1:
            board[i[1]:i[3]+1,i[2]:i[4]+1] -= i[5]
            # for j in range(i[1],i[3]+1):
            #     for k in range(i[2],i[4]+1):
            #         board[j][k] -= i[5]
        if i[0] == 2:
            board[i[1]:i[3]+1,i[2]:i[4]+1] += i[5]
            # for j in range(i[1],i[3]+1):
            #     for k in range(i[2],i[4]+1):
            #         board[j][k] += i[5]
    
    cnt = 0 # 기껏해야 1만번 실행.. 건들필요 없음.
    for i in board:
        for j in i:
            if j > 0:
                cnt += 1
    # cnt = 0
    # for i in sum(board,[]):
    #     if i > 0:
    #         cnt += 1 
    return cnt
    
# ! second.. fail..!..

# 참고글 : https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/