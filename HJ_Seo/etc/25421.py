# https://www.acmicpc.net/problem/25421

num = [1 for _ in range(9)]

n = int(input())

while n != 1:
    tmp = []
    for i in range(9):
        tmp.append(sum(num[max(0,i-2):min(10,i+3)])%987654321)
    num = tmp
    n -= 1

print(sum(num)%987654321)



'''
1 1 1 1 1 1 1 1 1 - 1
3 4 5 5 5 5 5 4 3 - 2
'''