# https://www.acmicpc.net/problem/1074

# N,r,c = map(int,input().split())

# result = 0
# for i in range(N+1):
#     if r & (1<<i):
#         result += 2*4**i
#     if c & (1<<i):
#         result += 4**i

# print(result)

# ! 아래는 압축!

n,r,c=map(int,input().split())
a=0
for i in range(n+1):
    if r&(1<<i):a+=2*4**i
    if c&(1<<i):a+=4**i
print(a)
 