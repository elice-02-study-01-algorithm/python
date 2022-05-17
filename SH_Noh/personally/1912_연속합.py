# 124ms
from sys import stdin

input = stdin.readline
n = int(input())
sequence = list(map(int, input().split()))

sum = [0] * n
sum[0] = sequence[0]

for i in range(1, n):
    sum[i] = max(sum[i-1] + sequence[i], sequence[i])

print(max(sum))

'''신기한 출력 방법, 112ms
import sys

def main(input=sys.stdin, output=sys.stdout):
    N = int(input.readline())
    maximum = None
    sum = 0
    for i in map(int, input.readline().split()):
        sum += i
        if maximum == None or maximum < sum:
            maximum = sum
        sum = max(0, sum)
    output.write(f'{maximum}\n')

if __name__ == '__main__':
    main()
'''