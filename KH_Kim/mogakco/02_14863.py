# 백준 14863
# 서울에서 경산까지
# DP

# 전체모금액을 가능한 많이 얻는 방법
# 시간 K분으로 한정
# -> 제한 시간 이내로 서울에서 경산까지 여행하면서 모금할 수 잇는 최대 금액

# 입력
# N(도시의개수),K(제한시간)
# 도보( 이동시간, 모금액), 자전거( 이동시간, 모금액)
# N+1줄

# 출력
# K분 이내 여행하며 모금 최대 금액
'''
예제1)
200(도) + 370 + 250 = 820

K 1650
1,2(도), 3(자) 모금  660 |시간 1600


예제2) K 3000
도) 시 4200 | 금액 80

'''
import sys

N, K = map(int, sys.stdin.readline().split())
# data = [sys.stdin.readline().strip() for i in range(N)]
data = []
for i in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))


print(N)
print(data)

# 도보 금액 시간으로 나눈 비율
do_rate = [data[i][1] / data[i][0] for i in range(N)]
print(do_rate)

# 자전거 금액 시간으로 나눈 비율
ja_rate = [data[i][3] / data[i][2] for i in range(N)]
print(ja_rate)

# 도보 정렬
do_sort = sorted(do_rate)
print('정렬', do_sort)

# 시간계산
result_time = 0
result_mon = 0
# while True:
for i in range(N):
    result_time += data[i][0]
    result_mon += data[i][1]
print(result_time)
print(result_mon)
if result_time < K:
    print('성공: ', result_time)
else:
    tempIndex = do_rate.index(min(do_rate))
    print('tem', tempIndex)

    # 도로 빼기
    result_time -= data[tempIndex][0]
    result_mon -= data[tempIndex][1]
    print(result_time)
    print(result_mon)
    # 자전거 추가
    result_time += data[tempIndex][2]
    result_mon += data[tempIndex][3]
    print('else:', result_time)
    print('money', result_mon)


'''
도보가 자전거 모다 모금액이 더 많이 모임
도보로 했을때 시간 초과가 될경우
계산한 do_rate 중 가장 낮은 값을 우선적으로 자전거로 대체
그래도 시간 초과시 다음 낮은 순위의 do_rate를 자전거로 대체 (반복)
'''
# if __name__ == '__main__':
