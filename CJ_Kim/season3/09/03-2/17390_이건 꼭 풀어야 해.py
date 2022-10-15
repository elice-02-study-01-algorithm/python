import sys
input = sys.stdin.readline

seqNum, questionNum = map(int, input().split())
initSeq = [0 for _ in range(1001)]
# initSeq = [0]*1001 (감사해요 정윤님!)

sortedSeq = sorted(list(map(int, input().split())))

prefixSum = [0]

# 누적합 리스트 별도로 생성하기
for i in range(len(sortedSeq)):
    prefixSum.append(prefixSum[i]+sortedSeq[i])
# 예제 1의 경우 - [0, 1, 3, 6, 10, 15]
# 예제 2의 경우 - [0, 1, 3, 5, 8, 13]

for _ in range(questionNum):
    i, j = map(int, input().split())
    print(prefixSum[j]-prefixSum[i-1])