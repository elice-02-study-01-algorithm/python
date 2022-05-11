# 1,2,3 더하기.
'''
P(n) = P(n-1)+P(n-2)+P(n-3) 
basis : P(1) = 1 - 1, P(2) = 2 - 1, P(3) = 4 - 1
'''
T = int(input())
sum_lst = [0,1,2,4]

for _ in range(T):
    n = int(input())
    if len(sum_lst)<3:
        print(sum_lst[n]-1)
    elif len(sum_lst)>n:
        print(sum_lst[n])
    else:
        for i in range(3,n):
            sum_lst.append(sum_lst[-3]+sum_lst[-2]+sum_lst[-1])
        print(sum_lst[n])
# print(sum_lst)

