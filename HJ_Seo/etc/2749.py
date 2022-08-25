# https://www.acmicpc.net/problem/2749

n = int(input())%1500000 # 1500000에서 1,2번째 피보나치 수가 반복됨. 

tmp1 = 1
tmp2 = 0
while n != 1:
    
    tmp1,tmp2 = (tmp1+tmp2)%1000000,tmp1
    
    n -= 1
    
print(tmp1)

# 10826번 99%에서 시간초과??...