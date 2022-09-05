# 시간초과 45/100
# 이진탐색으로 헤보려다가 로직 꼬여서 포기
# 아래는 정답 코드가 아님
import sys
def main():
    emp = int(sys.stdin.readline())
    house = list(map(int, sys.stdin.readline().split()))
    minDis = emp*max(house)
    start = min(house)
    end = max(house)
    while True:
        if start == end:
            break
        mid = (start+end)//2
        distanceSum = 0
        for employee in house:
            distanceSum += abs(employee-mid)
        if distanceSum < minDis:
            minDis = distanceSum


if __name__=="__main__":
    main()