import sys

seqLen = int(sys.stdin.readline())
seqList = list(map(int, sys.stdin.readline().split()))

def countLen(seqList):
    # 증가, 감소 각각 저장하는 리스트를 따로 만든다.
    # 증가하는 수열의 길이 저장하는 리스트
    incCnt = [1]
    # 감소하는 수열의 길이 저장하는 리스트
    decCnt = [1]
    for i in range(1, len(seqList)):
        # 이전 것이 지금 것보다 작기만 하면,
        # 증가하는 수열의 길이만 늘리고, 감소는 1로 초기화
        if seqList[i]<seqList[i-1]:
            decCnt.append(decCnt[-1]+1)
            incCnt.append(1)
        # 이전 것이 지금 것보다 크기만 하면,
        # 감소하는 수열의 길이만 늘리고, 증가는 1로 초기화
        elif seqList[i]>seqList[i-1]:
            incCnt.append(incCnt[-1]+1)
            decCnt.append(1)
        # 서로 같으면 둘다 늘리기
        else:
            decCnt.append(decCnt[-1]+1)
            incCnt.append(incCnt[-1]+1)
    return max(max(incCnt), max(decCnt))

print(countLen(seqList))