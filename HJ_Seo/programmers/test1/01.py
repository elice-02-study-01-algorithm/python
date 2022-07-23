# 1번.

def solution(X, Y):
    arr = {str(i):0 for i in range(10)}
    arr2 = {str(i):0 for i in range(10)}

    for i in X:
        arr[i] += 1
    
    for i in Y:
        if arr[i] != 0:
            arr[i] -= 1
            arr2[i] += 1
    
    temp = 0
    for i in ['9','8','7','6','5','4','3','2','1']:
        temp += arr2[i]
    
    if temp + arr2['0'] == 0:
        return '-1'
    
    elif arr2['0'] != 0 and temp == 0:
        return '0'

    answer = ''
    for i in ['9','8','7','6','5','4','3','2','1','0']:
        answer += i*arr2[i]
    return answer

