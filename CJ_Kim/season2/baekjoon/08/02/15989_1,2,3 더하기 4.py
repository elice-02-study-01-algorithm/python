'''
T(1) = 1 / 1
T(2) = 2 / 1 + 1, 2
T(2) = 1 + T(1) 

       1 + 1

       2

T(3) = 3 / 1 + 1 + 1, 1 + 2, 3
T(3) = 1 + T(2) + T(1) - 1

       1 + (2)
       1 + 1 + 1

       3
       
[0, 0, 1]
T(4) = 4 / 1 + 1 + 1 + 1, 2 + 1 + 1, 2 + 2, 1 + 3
T(4) = 3T(1) + 2T(2)
       1 + 2 + 1(1 + 1 + 1 + 1)

       1 + (3)
       1 + 1 + (2)
       1 + 1 + 1 + 1

       2 + 2

T(5) = 3T(2) + 2T(3)
       2 + 3 + 1
       3 + (1 + 1 / 2), 2 + (1 + 1 + 1 / 1 + 2 / 3), 1 + 1 + 1 + 1 + 1

       1 + ( 2 + 2 4[2]+4[3])     1
       1 + 1 + ( 3 3[2]+3[3])     1

       1 + 1 + 1 (2 == 2[2])      1
       1 + 1 + 1 + 1 + 1          1

       2 + (3== 3[3])       1

T(6) = 
      1 + (5[2]+5[3])              1
      1 + 1 + (4[2]+4[3])          1
      1 + 1 + 1 + (3[2]+3[3])      1
      1 + 1 + 1 + 1 + (2[2]+2[3])  1
      1 + 1 + 1 + 1 + 1 + 1        1

      2 + (4[3])                   0
      2 + 2 + (2[3])               0
      2 + 2 + 2                    1

      3 + 3                        1

T(7) = 
      1 + (6[2]+6[3])                 2
      1 + 1 + (5[2]+5[3])             1
      1 + 1 + 1 + (4[2]+4[3])         1
      1 + 1 + 1 + 1 + (3[2]+3[3])     1
      1 + 1 + 1 + 1 + 1 + (2[2]+2[3]) 1
      1 + 1 + 1 + 1 + 1 + 1 + 1

      2 + ([5[3])                     0
      2 + 2 + (3[3])                  1

T(N) = for i in range(N-1, 1) sum(i[2]+i[3])
     + for j in range(N-2, 2 or 3 , -2) sum(j[3])
     + 1 if N % 3 == 0 else 0

'''

# 시간 초과난 코드입니다
# 형준님과 아이디어는 유사합니다!
import sys
input = sys.stdin.readline

testCaseNum = int(input())

T = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 2, 0, 1]]

# 메모이제이션 방법
def oneTwoThreeOp(num):
    if num<4:
        return sum(T[num])
    
    # 이미 만들어진 N이라면 바로 반환
    if len(T)>num:
        return sum(T[num])

    for i in range(len(T), num+1):
        # 1이 반드시 들어가는 경우
        oneOp = 1
        # 1이 없는 경우
        twoOp = 0
        if i%2==0:
            twoOp += 1
        # 1, 2가 없는 경우
        threeOp = 0

        for j in range(i-1, 0, -1):
            oneOp+=T[j][2]+T[j][3]
        
        for k in range(i-2, 0, -2):
            twoOp+=T[k][3]

        # 3으로만 구성된 경우 하나 늘려주기
        if i % 3 == 0:
            threeOp += 1
        T.append([0, oneOp, twoOp, threeOp])
        
    return sum(T[num])
        

for i in range(testCaseNum):
    inputNum = int(input())
    answer = 0
    if len(T)-1<inputNum:
        answer = oneTwoThreeOp(inputNum)
    else:
        answer = sum(T[inputNum])
    print(answer)


'''
미완성 코드이니 코드리뷰 안하셔도 됩니다!
import sys
input = sys.stdin.readline

testCaseNum = int(input())

plusCase = [[1, 0, 0]]*(10001)
plusCase[2] = [1, 1, 0]
print(plusCase)
for i in range(3, 10):
    # print('---------i----------', i, plusCase[:5])
    print(i, plusCase[:10], plusCase[i-2][0], plusCase[i-2][1])
    plusCase[i][1] = plusCase[i-2][0]+plusCase[i-2][1]
    print(plusCase[:10])
    #plusCase[i][2] += plusCase[i-3][0]+plusCase[i-3][1]+plusCase[i-3][2]
print(plusCase[:5])
for _ in range(testCaseNum):
    print(sum(plusCase[int(input().strip())]))

'''