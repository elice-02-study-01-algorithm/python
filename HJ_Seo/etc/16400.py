'''
2 --> 1 : 2
3 --> 1 : 3
4 --> 1 : 2+2 
5 --> 2 : 2+3 5
6 --> 2 : 2+2+2 3+3
7 --> 3 : 3+2+2 5+2 7
8 --> 3 : 2+2+2+2 3+3+2 5+3 
9 --> 4 : 7+2 5+2+2 3+3+3 3+2+2+2
10 --> 5: 7+3 5+5 5+3+2 3+3+2+2 2+2+2+2+2
...
30 --> 23+7 23+5+2 23+3+2+2 19+7+2+2 19+5+3+3 19+5+2+2+2 17+ 

'''
import math

def isPrime(n):
    if n == 2 or n == 3:
        return True
    
    k = int(math.sqrt(n))
    
    for i in range(2,k+1):
        if n%i == 0:
            return False
    
    return True

n = int(input())

Prime = []

for i in range(2,n+1):
    if isPrime(n):
        Prime.append(i)


Pnum = [0,1,1]

#! 이게 무슨 원리이려나?..
 