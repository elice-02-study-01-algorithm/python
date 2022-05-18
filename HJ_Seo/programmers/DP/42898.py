# 웅덩이
## 효율성 0점..?...,,,, 구하는 값이 나머지여서,,,ㅠ

def solution(m, n, puddles):
    hsroad = [[0]*(m+1) for _ in range(n+1)]
    hsroad[1][1] = 1

    # for i in hsroad:
    #     print(i)
    # print('==================')
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if i == 1 and j == 1:
                continue
            if [i,j] in puddles:
                hsroad[j][i] = 0
            else:
                hsroad[j][i] = hsroad[j-1][i] + hsroad[j][i-1]

    # for i in hsroad:
    #     print(i)

    return hsroad[-1][-1]%1000000007

m,n = map(int,input().strip().split())
puddles = [[2,2]]

print(solution(m, n, puddles))

