# def solution(topping):
#     answer = 0
#     for i in range(1, len(topping)):
#         l, r = topping[0:i], topping[i:len(topping)]
#         l, r = set(l), set(r)
#         if len(l) == len(r):
#             answer += 1
        
#     return answer

# 엄청난 시간초과!
# 어찌보면 당연한 결과!

def solution(topping):
    answer = 0
    length = len(list(set(topping)))
    set_1 = [0 for i in range(length + 1)]
    set_2 = [0]
    
    for i in range(len(topping)):
        set_1[topping[i]] += 1
    print("최초 set_1: ", set_1)
    for i in range(len(topping)):
        set_1[topping[i]] -= 1
        print("set_1: ", set_1)
        if set_1[topping[i]] == 0:
            length -= 1
        set_2[topping[i]] += 1
        if length == len(set_2):
            answer += 1
        
    return answer

solution([1, 2, 1, 3, 1, 4, 1, 2])

# 틀림!