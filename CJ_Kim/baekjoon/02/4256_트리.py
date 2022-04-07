testCaseNum = int(input())
global answer
answer = []
def makeList(list):
    answerList = []
    for i in list:
        if i==None:
            pass
        elif type(i)!=int:
            answerList+=i
        else:
            answerList.append(i)
    return answerList


def postOrder(preOrder, inOrder):
    global answer
    if len(preOrder)==0:
        return
    if len(preOrder)==2:
        return [preOrder[-1], preOrder[0]]
    if len(preOrder)==1:
        return preOrder[0]
    
    pivot = preOrder[0]
    tempInOrder = inOrder[:inOrder.index(pivot)]
    tempPreOrder = preOrder[1:(len(tempInOrder)+1)]

    left = postOrder(tempPreOrder, tempInOrder)
    answer.append(left)
    right = postOrder(preOrder[len(tempInOrder)+1:], inOrder[inOrder.index(pivot)+1:])

    answer.append(right)
    answer.append(pivot)

    return 


for _ in range(testCaseNum):
    answer = []
    totalNum = int(input())
    postOrderList = []
    preOrderList = list(map(int, input().split()))
    inOrderList = list(map(int, input().split()))
    postOrder(preOrderList, inOrderList)
    postOrderList = makeList(answer)
    print(*postOrderList)

# 6 2 1 4 3 5 7 9 8
# 1 2 3 4 5 6 7 8 9 
# 1 3 5 4 2 8 9 7 6