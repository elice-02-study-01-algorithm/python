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

import sys
input = sys.stdin.readline

testCaseNum = int(input())

T = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 2, 0, 1]]

def oneTwoThreeOp(num):
    if num<4:
        return sum(T[num])
    if len(T)>num:
        return sum(T[num])
    for i in range(len(T), num+1):
        oneOp = 1
        twoOp = 0
        if i%2==0:
            twoOp += 1
        threeOp = 0
        for j in range(i-1, 0, -1):
            # print('in j', i, j, T[j])
            oneOp+=T[j][2]+T[j][3]
        for k in range(i-2, 0, -2):
            # print('this is', i, k, T[k])
            twoOp+=T[k][3]
        if i % 3 == 0:
            threeOp += 1
        # print('in num', i, oneOp, twoOp, threeOp)
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
# print(T)

# 시간 초과