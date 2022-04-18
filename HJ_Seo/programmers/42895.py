#으로 표현
"""
초기값은..?
P[1] = [N]
P[2] = list(set([NN,N+N,N*N,1]) or list(set([11,2])(N==1)

for i in range(3,8):
    for j in range(1,i//2):
        P[i] += P[j]^P[i-j]   ~~~~~ ^ : 모든 연산.. 따로 함수를 만들어야 함.
    
    if number in P[i]:
        return i

return -1

"""

def solution(N,number):
    def induction_sim(lst1,lst2, sumlst):
        result_lst = []
        for i in lst1:
            for j in lst2:
                if i+j not in sumlst:
                    result_lst.append(i+j)
                
                if i-j > 0 and i-j not in sumlst:
                    result_lst.append(i-j)
                if j-i > 0 and j-i not in sumlst:
                    result_lst.append(j-i)

                if i*j not in sumlst:
                    result_lst.append(i*j)
                
                if i%j==0 and i//j not in sumlst:
                    result_lst.append(i//j)
                if j%i==0 and j//i not in sumlst:
                    result_lst.append(j//i)
        
        result_lst = list(set(result_lst))
        return result_lst

    lst = [[0]]
    for i in range(8):
        lst.append([])

    #basis step.
    lst[1].append(N)
    lst[2] = [N*11,N+N,N*N,N//N]
    lst[2] = list(set(lst[2]))
    if N in lst[2]:
        lst[2].remove(N)
    
    # print(1,lst[1])
    # print(2,lst[2])
    if number in lst[1]:
        return 1
    elif number in lst[2]:
        return 2

    for i in range(3,9):
        sum_lst = sum(lst,[]) #불필요한 것이 추가로 들어가는 것을 방지하기 위한 대비.
        for j in range(1,i//2+1):
            lst[i]+= induction_sim(lst[j],lst[i-j],sum_lst)
        
        # print(i,lst[i])
        if number in lst[i]:
            return i
    
    return -1


N = int(input())
number = int(input())
print(solution(N,number))