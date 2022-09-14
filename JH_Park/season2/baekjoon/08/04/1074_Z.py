import sys
input = sys.stdin.readline

n, r, c = map(int, sys.stdin.readline().split())
# 2 3 1
result = 0
  
while n > 0:
    n -= 1
    cmp = 2 ** n
    # n = 1
    # cmp = 2 ^ 1 = 2
    
    # n = 0
    # cmp = 2 ^ 0 = 1
    
    # 1 사분면
    if r < cmp and c < cmp:
        pass
    # 2 사분면
    elif r < cmp and c >= cmp:
        result += cmp ** 2
        c -= cmp
        # print("2사", result)
    # 3 사분면
    elif r >= cmp and c < cmp:
        result += cmp * (cmp * 2)
        r -= cmp
        # print("3사", result)
    # 4 사분면
    else:
        result += cmp * (cmp * 3)
        r -= cmp
        c -= cmp
        # print("4사", result)
print(result)

# n = 2
# 2**2 => 4 x 4
# 1사분면
# row : 가로 < 2 ** (n - 1) and col: 세로 < 2 ** (n - 1)
# row : 가로 < 2 and 세로 < 2

# 2사분면
# row : 가로 < 2 ** (n - 1) and col: 세로 >= 2 ** (n - 1)
# row : 가로 < 2 and col : 세로 >= 2

# 3사분면
# row : 가로 >= 2 ** (n - 1) and col: 세로 < 2 ** (n - 1)
# row : 가로 >= 2 and col : 세로 < 2

# 4사분면
# row : 가로 >= 2 ** (n - 1) and col: 세로 >= 2 ** (n - 1)
# row : 가로 >= 2 and col : 세로 >= 2