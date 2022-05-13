# 실험성 코드 페이지입니다. 백준이나 프로그래머스, 앨리스 문제 풀이 파일이 아녜요! - HJ -
#한글문서는 오픈 안됨.

import functools, itertools, random, math, time
import numpy as np #pandas, matplotlib 안깔림 

# 17366.

# 1654.
from sys import stdin

K,N = map(int,input().strip().split())
lines = []
for _ in range(K):
    lines.append(int(stdin.readline().strip()))
    
print(lines)

maxi = 1

# dlines = [i//maxi for i in lines]
# sum(dlines) >= K
# max(maxi) = ?