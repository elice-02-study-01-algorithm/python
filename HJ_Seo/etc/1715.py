import heapq

n = int(input())

q = []
for _ in range(n):
    heapq.heappush(q,int(input()))
    
if n == 1:
    print(heapq.heappop(q))
    exit()

result = 0
for _ in range(n-1):
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    result += a+b
    heapq.heappush(q,a+b)
print(result)
