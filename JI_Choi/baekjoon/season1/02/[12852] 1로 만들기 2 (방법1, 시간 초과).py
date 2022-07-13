import sys

N = int(sys.stdin.readline().rstrip())
# d는 최솟값을 입력받는 배열
d = [0] * N
# l은 이전경로를 입력받는 배열
l = [0] * N

def makeOne(n):
  # n이 1인 경우
  if n==1:
    d[n-1] = 0
    l[n-1] = 0
    return d[n-1]

  # n이 2인 경우
  elif n==2 or n==3:
    d[n-1] = 1
    l[n-1] = 1
    return d[n-1]

  elif d[n-1] != 0:
    return d[n-1]

  # n이 3의 배수이며, 2의 배수는 아닌 경우
  elif n%3==0 and n%2!=0:
    if makeOne(n//3) <= makeOne(n-1):
      d[n-1] = makeOne(n//3) + 1
      l[n-1] = n//3
      return d[n-1]
    else:
      d[n-1] = makeOne(n-1) + 1
      l[n-1] = n-1
      return d[n-1]
  
  # n이 3의 배수는 아니며, 2의 배수인 경우
  elif n%3!=0 and n%2==0:
    if makeOne(n//2) <= makeOne(n-1):
      d[n-1] = makeOne(n//2) + 1
      l[n-1] = n//2
      return d[n-1]
    else:
      d[n-1] = makeOne(n-1) + 1
      l[n-1] = n-1
      return d[n-1]
  
  # n이 3의 배수도 아니고, 2의 배수도 아닌 경우
  elif n%3!=0 and n%2!=0:
    d[n-1] = makeOne(n-1)+1
    l[n-1] = n-1
    return d[n-1]
  
  # n이 6의 배수인 경우
  else:
    group = min(makeOne(n//3), makeOne(n//2), makeOne(n-1))
    if makeOne(n//3) == group:
      d[n-1] = makeOne(n//3) + 1
      l[n-1] = n//3
      return d[n-1]
    elif makeOne(n//2) == group:
      d[n-1] = makeOne(n//2) + 1
      l[n-1] = n//2
      return d[n-1]
    elif makeOne(n-1) == group:
      d[n-1] = makeOne(n-1) + 1
      l[n-1] = n-1
      return d[n-1]

# 연산을 하는 횟수의 최솟값 구하기
for i in range(1,N+1):
  makeOne(i)
print(d[N-1])
# N을 1로 만드는 방법에 포함되어 있는 수 출력
print(N, end=' ')
path = []
while True: 
  path.append(l[N-1])
  if l[N-1] == 1:
    break
  N = l[N-1]

print(*path)