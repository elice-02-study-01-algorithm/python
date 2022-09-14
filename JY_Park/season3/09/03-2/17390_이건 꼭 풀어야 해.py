import sys
input = sys.stdin.readline

def solution():
    n, q = map(int,input().split())
    nums = sorted(list(map(int,input().split())))
    
    sum_value = 0
    prefix_sum = [0]
    for i in nums:
        sum_value += i
        prefix_sum.append(sum_value)

    for i in range(q):
        l, r = map(int,input().split())
        print(prefix_sum[r] - prefix_sum[l-1])

if __name__ == '__main__':
    solution()

# 배열의 맨 앞부터 특정 위치까지의 합을 미리 구해 놓음 
# 1 2 3 4 5
# 1 3 6 10 15