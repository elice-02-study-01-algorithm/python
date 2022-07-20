def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    
    for s in skill:
        t = s[0]
        r1 = s[1]
        c1 = s[2]
        r2 = s[3]
        c2 = s[4]
        degree = s[5]
        if t == 1:
        #  (0, 0), (3, 4) 
            for row in range(r1, r2 + 1):
                for col in range(c1, c2 + 1):
                    board[row][col] -= degree            
        else:
            for row in range(r1, r2 + 1):
                for col in range(c1, c2 + 1):
                    board[row][col] += degree
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 1:
                answer += 1
        
    return answer