N,M = map(int,input().strip().split())

if N>M:
    temp = N
    N = M
    M = temp
# Then, N <= M.

# # inital code.
result = 0

powerset = []
k = 0
while k**2< N*M:
    k += 1
    powerset.append(k**2)

for i in range(1,N+1):
    for j in range(i+1,N+1):
        if i*j in powerset:
            result += 1

result = 2*result + N

for i in range(1,N+1):
    for j in range(N+1,M+1):
        if i*j in powerset:
            result += 1

print(result)
# ======================
# 1. A == B case.

# 2. A != B case.