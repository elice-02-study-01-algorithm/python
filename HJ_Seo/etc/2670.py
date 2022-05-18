# #연속 부분 최대곱.
from sys import stdin

n = int(stdin.readline())
lst = [float(stdin.readline()) for _ in range(n)]

result = -1

for i in range(1,len(lst)):
    lst[i] = max(lst[i],lst[i]*lst[i-1])

# print(lst)
result = round(max(lst),3)

print("%.3f" % (result))

#### 이거 왜 시간 초과가 나오는지 이해가 안되네,,,,


# N = int(input())
# li = [float(input()) for _ in range(N)]
# print(li)
# for i in range(1, N):
#     li[i] = max(li[i], li[i]*li[i-1])
# print(li)
# print("%.3f" % (max(li)))