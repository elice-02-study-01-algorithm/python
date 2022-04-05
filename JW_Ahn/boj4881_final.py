# 자리수의 제곱합 구하는 함수
def squaredSum(num) :
  num = str(num)
  next = 0
  
  for i in range (len(num)):
      next += int(num[i]) * int(num[i])
  
  return next

# case2: 사이클 밖에서 만날 경우
def isSame(arr1, arr2) :
  for i in range(len(arr1)) :
    if arr1[i] in arr2 :
      return i + 2 + arr2.index(arr1[i])
  else :
    for i in range(len(arr2)) :
      if arr2[i] in arr1 :
        return i + 2 + arr1.index(arr2[i])
      
  return False

def minRoute(num1, num2) :
  route1 = abs(cycle.index(num1) - cycle.index(num2))
  route2 = len(cycle) - max(cycle.index(num1), cycle.index(num2)) + min(cycle.index(num1), cycle.index(num2))
  return min(route1, route2)

cycle = [4, 16, 37, 58, 89, 145, 42, 20]

# 0 0 을 입력받으면 종료
while True :
  A, B = map(int, input().split())

 # 0이 하나라도 입력됨
  if A == 0 and B == 0 :
    break
  elif A == 0 or B == 0 :
    print(A, B, 0)
  
  # 자릿수의 제곱합 배열 초기화
  sum1, sum2 = [A], [B]

  while sum1[-1] not in cycle and sum1[-1] != 1:
    next = squaredSum(sum1[-1])
    sum1.append(next)
    # print("sum1 :", sum1)
  
  while sum2[-1] not in cycle and sum2[-1] != 1:
    next = squaredSum(sum2[-1])
    sum2.append(next)
    # print("sum2 :", sum2)
  
  # case1 : 서로 다른 cycle에 있을 경우
  if sum1[-1] in cycle and sum2[-1] == 1 :
      print(A, B, 0)
  elif sum2[-1] in cycle and sum1[-1] == 1 :
    print(A, B, 0)
  
  # case2 : 사이클 밖에서 만날 경우
  elif isSame(sum1, sum2) :
    print(A, B, isSame(sum1, sum2))

  # case3 : 둘 다 사이클에 있을 경우 차이를 더해줌
  elif sum1[-1] in cycle and sum2[-1] in cycle :
    chayi = minRoute(sum1[-1], sum2[-1])
    print(A, B, len(sum1) + len(sum2) + chayi)
