import sys
input  = sys.stdin.readline

def solution():
    while True:
        n = int(input())
        p = [int(input()) for i in range(n)]

        # sum_value = 0
        # sum_max = 0
        
        if n == 0:
            break

        for i in range(1,n):
            if p[i] < p[i] + p[i-1]:
                p[i] = p[i] + p[i-1]

        # for i in range(n):
        #     sum_value = 0
        #     sum_max = 0
        #     for j in range(i, n):
        #         sum_value += p[j]
        #         if sum_value > sum_max: 
        #             sum_max = sum_value

        # print(sum_max)
        
        print(max(p))
        

if __name__ == '__main__':
    solution()