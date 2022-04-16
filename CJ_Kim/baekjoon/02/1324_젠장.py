# 엉망진창 코드~
# 뚝딱거리는 중~

# def LCS(s1, s2):
#     m = len(s1)
#     n = len(s2)
#     L = [[None]*(n+1) for i in range(m+1)]

#     for i in range(m+1):
#         for j in range(n+1):
#             if i == 0 or j == 0:
#                 L[i][j] = 0
#             elif s1[i-1] == s2[j-1]:
#                 L[i][j] = L[i-1][j-1]+1
#             else:
#                 L[i][j] = max(L[i-1][j], L[i][j-1])
    
#     return L[m][n]
    
def LIS(myData) :
    
    L = [0] * len(myData)
    ascendingList = [[] for _ in range(len(myData))]
    for n in range(len(myData)):
        ascendingList[n].append(n)
        for i in range(n):
            if myData[i] <= myData[n]:
                L[n] = max(L[n], L[i]+1) 
                ascendingList[n].append(myData[i])           
    print(ascendingList)
    return max(L)+1

# print(LCS([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]))
LIS([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])

# list01 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list02 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

# sortedList01 = []

# for index, value in enumerate(list02):
#     sortedList01.append((index, value))

# sortedList01 = sorted(sortedList01, key=lambda x: x[1])
# print(sortedList01)