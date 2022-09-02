# 효율성 실패 풀이

# def solution(board, skill):
#     answer = 0
    
#     for s in skill:
#         type, r1, c1, r2, c2, degree = s
#         for row in range(r1, r2+1):
#             for col in range(c1, c2+1):
#                 if type == 1:
#                     board[row][col] -= degree
#                 else:
#                     board[row][col] += degree

#     for b in board:
#         answer += len(list(filter(lambda x: x > 0, b)))

#     return answer