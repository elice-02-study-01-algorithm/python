import math

def solution(n, m):
    # n = 2 case.. prime
    # n = 3 case.. prime square.
    # n = 4 case.. multiple dist.prime.... 세제곱도 있지..
    num2 = []
    num4 = []
    def is_Prime(n,alreadPrime):
        for i in alreadPrime:
            if n%i == 0:
                return False
        return n
    Prime = [2]
    k = 3
    while True:
        if len(Prime) == 3000:
            break
        
        x = is_Prime(k,Prime)
        if x:
            Prime.append(x)

        k += 1

    if n == 2:
        return Prime[m-1]
    elif n == 3:
        return Prime[m-1]**2

    x = []
    for i in range(1999):
        x.append(Prime[i]**3)
        for j in range(i+1,2000):
            x.append(Prime[i]*Prime[j]) # ! 대강 적정숫자는 어느정도일까??...
    
    print(x[:10])
    return sorted(x)[m-1]
