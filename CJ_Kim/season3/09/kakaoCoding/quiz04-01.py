# 미완성 코드예요!
def makeBinaryTree(number):
    binaryLength = 1
    binaryOriginNumber = len(str(format(number, 'b')))
    while True:
        if 2**binaryLength-1>=binaryOriginNumber:
            break
        binaryLength+=1
    nodeNumber = 2**binaryLength-1
    binaryNumber = str(format(number, 'b'))
    while len(binaryNumber)<nodeNumber:
        binaryNumber = '0'+binaryNumber
    print('binaryNumber', binaryNumber)
    return binaryNumber

def isBinaryTree(number):
    for i in range(len(number)):
        if (i+1)%2==0 and number[i]=='0':
            if number[i-1]=='0' and number[i+1]=='0':
                pass
            else:
                return False
    return True

def solution(numbers):
    answer = []
    for number in numbers:
        if isBinaryTree(makeBinaryTree(number))==False:
            answer.append(0)
        else:
            answer.append(1)
    return answer

print(solution([7, 5]))
print(solution([63, 111, 95]))
print(solution([32767, 16383, 24575]))
# 111111111111111, 011111111111111, 101111111111111
print(solution([30975, 30848]))
# 111100011111111, 111100010000000
print(solution([119, 28927]))
# 1110111, 111000011111111
print(solution([79, 104]))
# 1001111, 1101000
print(solution([32647 ,32655, 32654]))
# 111111110000111, 111111110001111
print(solution([128, 2, 4, 8, 16]))
# 010, 00100, 0001000, 000010000
print(solution([22015]))
# 101010111111111


# 중위순회
def inOrder(start):
    result = ''
    node = start
    if node == '.':
        return ''
    if treeDic[node]:
        result += inOrder(treeDic[node][0])
        result += node
        result += inOrder(treeDic[node][1])
    return result