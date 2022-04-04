# from itertools import combinations
# numList = [i for i in range(1, 81)]

# newNumList = []
# for i in numList:
#     newNumList.append(i*i)
# resultList = list(combinations(newNumList ,2))

# finalList = []
# for n in resultList:
#     x, y = n
#     finalList.append(x+y)
# print(sorted(finalList))

def makeDoubleSum(num):
    numList = []
    
    for i in str(num):
        numList.append(int(i)^2)