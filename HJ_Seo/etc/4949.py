from sys import stdin
from collections import deque
import re

while True:
    Q = deque()
    check1 = 0
    dic = {')':'(',']':'['}

    arr = stdin.readline().rstrip()
    if arr == '.':
        break
    
    x = re.findall('[\[\]\(\)]',arr)
    for i in range(len(x)):
        if x[i] == '(':
            Q.append('(')
        elif x[i] == '[':
            Q.append('[')
        else:
            if len(Q) == 0:
                print('no')
                check1 = 1
                break
            
            temp = Q.pop()
            if dic[x[i]] != temp:
                check1 = 1
                print('no')
                break
    
    if check1 == 0 and len(Q) == 0:
        print('yes')
    elif check1 == 0:
        print('no')
    