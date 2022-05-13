# 도둑질
# 타입 2개.. P[1:],P[:-1] 로 나눈후 마지막에 max.
# 최대 크기 100만개라는 것이 맘에 걸린다..

def solution(money):
    if len(money) == 3:
        return max(money)

    def still_max(lst):
        lst[2] += lst[0]
        for i in range(3,len(lst)):
            lst[i] += max(lst[i-2],lst[i-3])
        return max(lst)

    money1 = money[1:]
    money2 = money[:-1]

    answer = max(still_max(money[1:]),still_max(money[:-1]))
    return answer


print(solution([90,0,0,95,1,1])) #185