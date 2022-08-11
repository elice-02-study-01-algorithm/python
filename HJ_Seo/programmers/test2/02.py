# def solution(topping):
#     answer = 0
    
#     for i in range(len(topping)-1):
#         if len(set(topping[:i])) == len(set(topping[i:])):
#             answer+=1
#     return answer

# ! initial code.. but 시간초과.

def solution(topping):
    answer = 0
    
    def move_left_to_right(left,right,num):
        if num not in right:
            right[num] = 1
        else:
            right[num] += 1
        
        if left[num] == 1:
            del left[num]
        else:
            left[num] -= 1
        return    

    left = dict()
    right = dict()
    for i in topping:
        if i not in left:
            left[i] = 1
        else:
            left[i] += 1
    
    for i in range(len(topping)):
        if len(left) == len(right):
            answer += 1
        move_left_to_right(left,right,topping[i])
    
    if len(left) == len(right):
            answer += 1 #마지막이 체크가 안되므로..

    return answer

# hash 이용, 통과.