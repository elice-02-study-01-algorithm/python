from itertools import product

# 1. 이모티콘 플러스 서비스 가입자를 최대한 늘리기
# 2. 이모티콘 판매액을 최대한 늘리기

def solution(users, emoticons):
    answer = []
    discounts = [10, 20, 30, 40]
    discounts_combi = sorted(list(product(discounts, repeat = len(emoticons))), reverse = True)
    max_join = 0
    max_profit = 0
    for discount in discounts_combi:
        purchase = [0] * len(users)
        join = 0
        # 사용자별로
        for i in range(len(users)):
            criteria, limit = users[i]
            # 기준에 따라 이모티콘 구매
            for j in range(len(discount)):
                if criteria <= discount[j]:
                    purchase[i] += emoticons[j] * (100 - discount[j]) / 100
            # 다 구매했는데 기준액 넘으면 이모티콘 플러스 가입
            if purchase[i] >= limit:
                join += 1
                purchase[i] = 0
        if max_join < join:
            max_join = join
            max_profit = sum(purchase)
        elif max_join == join:
            if sum(purchase) > max_profit:
                max_profit = sum(purchase)
            
    return [max_join, max_profit]