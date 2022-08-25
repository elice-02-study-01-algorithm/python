#  https://www.acmicpc.net/problem/6588

from sys import stdin

tmp = {i for i in range(2,1000000)}
Prime = set()
while True:
    if len(tmp) == 0:
        break
    x = tmp.pop()
    Prime.add(x)
    
    for i in range(x,1000000,x):
        tmp.discard(i)

while True:
    num = int(stdin.readline().strip())
    if num == 0:
        break
    
    for i in range(3, num//2+2,2):
        if i in Prime and num-i in Prime:
            print('{} = {} + {}'.format(num,i,num-i))
            break
    else:
        print("Goldbach's conjecture is wrong.")
