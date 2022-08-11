import sys
sys.setrecursionlimit(10**7)
# ! 아이디어가 있을텐데... 
def solution(arr):
    def check_pal(lst):
        if len(lst) == 1 or lst != lst[::-1]:
            return False
        
        return True
    
    def check_add_pal(arr,isTrue):
        if len(arr) == 1:
            return False
        elif isTrue == True:
            return True
        elif isTrue == False:
            if check_pal(arr):
                return True
        
        leng = len(arr)
        for i in range(leng-1):
            tmp = arr[:i] + [arr[i]+arr[i+1]] + arr[i+2:]
            if check_add_pal(tmp,isTrue):
                return True
        
        return False

    answer = 0
    leng = len(arr)
    for i in range(leng-1):
        for j in range(i+2,leng+1):
            tmp = arr[i:j]
            isTrue = False
            if check_add_pal(tmp,isTrue):
                answer += 1

    return answer
