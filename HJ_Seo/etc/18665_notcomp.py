# 1. target을 만들 수 있는 x,y를 우선 찾기.  z = x**2 - y
# 2. 각각의 x,y에 대해 x_1,y_1,x_2,y_2를 찾기.
# 3. 1,2,3으로 모두 만들 수 있을때까지..
# 4. 차례대로 x_n y_n \n x_n-1 y_n-1
#  ...... 프린트.

# 
import math

def get_xy(n):
    x = int(math.sqrt(n))+1
    y = n - x**2
    return x,y

S = [1,2,3]

n = int(input())
aim = [n]

x,y = get_xy(n)

