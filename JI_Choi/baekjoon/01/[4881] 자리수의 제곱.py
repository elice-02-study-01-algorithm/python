data = []
while True:
  a, b = map(int, input().split())
  if a == 0 and b == 0:
    break
  c = [a, b]
  data.append(c)

# 다음 수열을 구하는 함수
def nextSeq(num):
  splitString = list(str(num))
  splitNum = list(map(int, splitString))
  acc = 0
  for elem in splitNum:
    acc += elem**2
  return acc

### 최솟값 구하기 ###
for elem in data:
  # 순환하기 직전의 수열까지 구하기
  x = elem[0]
  list1 = [x]
  while True:
    if nextSeq(x) not in list1:
      list1.append(nextSeq(x))
      x = nextSeq(x)
    else:
      break

  # 순환하기 직전의 수열까지 구하기
  y = elem[1]
  list2 = [y]
  while True:
    if nextSeq(y) not in list2:
        list2.append(nextSeq(y))
        y = nextSeq(y)
    else:
      break

  # 1. 리스트의 마지막 원소가 각각 1과 1이 아닌 자연수인 경우
  if list1[-1] == 1 and list2[-1] != 1:
    print(list1[0], list2[0], 0)

  elif list1[-1] != 1 and list2[-1] == 1:
    print(list1[0], list2[0], 0)
  
  # 2. 그 외의 경우 
  else:
    pseudoAnswers = []
    # 유사 정답들을 리스트에 모으고, 정답(가장 작은 값)을 출력 
    for i in range(len(list1)):
      if list1[i] in list2:
        pseudoAnswer = i + list2.index(list1[i]) + 2
        pseudoAnswers.append(pseudoAnswer)

    print(list1[0], list2[0], min(pseudoAnswers))