# 실험성 코드 페이지입니다. 백준이나 프로그래머스, 앨리스 문제 풀이 파일이 아녜요! - HJ -
#한글문서는 오픈 안됨.

import functools, itertools, random, math, time
import numpy as np #pandas, matplotlib 안깔림 

# 17366.
from math import sqrt

A,B = map(int,input().strip().split())

result = 0

for i in range(1,A+1):
    for j in range(1,B+1):
        if sqrt(i*j)%1 == 0:
            print(i,j)
            result += 1

print(result)