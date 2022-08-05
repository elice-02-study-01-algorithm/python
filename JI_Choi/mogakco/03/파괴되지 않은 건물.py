# 2022 KAKAO BLIND RECRUITMENT
# 2022.07.17 10:05-10:45

def solution(board, skill):
    for info in skill:
        t, r1, c1, r2, c2, degree = info
        if t == 1:
            degree *= -1

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                board[i][j] += degree

    count = 0
    for i in board:
        for j in i:
            if j > 0:
                count += 1

    return count
