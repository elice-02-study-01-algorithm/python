def solution(number):
    answer = 0
    leng = len(number)
    tmp = 0
    for i in range(leng-2):
        tmp1 = tmp+number[i]
        for j in range(i+1,leng-1):
            tmp2 = tmp1+number[j]
            for k in range(j+1,leng):
                if tmp2+number[k] == 0:
                    answer+=1
    return answer
    