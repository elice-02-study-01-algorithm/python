import sys

N = int(sys.stdin.readline().rstrip())
d = [0] * (N+1)
l = [0] * (N+1)

# 연산을 하는 횟수의 최솟값 구하기
for i in range(2,N+1):
  d[i] = d[i-1] + 1
  l[i] = i-1
  # i가 2의 배수인 경우
  if i%2 == 0 and d[i//2] + 1 < d[i]:
    d[i] = d[i//2] + 1
    l[i] = i//2

  # i가 3의 배수인 경우
  # if ~ elif 문이 아닌, 두개의 if문을 사용
  if i%3 == 0 and d[i//3] + 1 < d[i]:
    d[i] = d[i//3] + 1
    l[i] = i//3

print(d[N])

# N을 1로 만드는 방법에 포함되어 있는 수 출력
print(N, end=' ')

while True:
  print(l[N], end=' ')
  if l[N] == 1:
    break
  N = l[N]