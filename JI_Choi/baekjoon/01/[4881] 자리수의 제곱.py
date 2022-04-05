data = []
while True:
  a, b = map(int, input().split())
  if a == 0 and b == 0:
    break
  c = [a, b]
  data.append(c)

# 다음 수열 구하기
def nextSeq(num):
  splitString = list(str(num))
  splitNum = list(map(int, splitString))
  acc = 0
  for elem in splitNum:
    acc += elem**2
  return acc

### 최솟값 구하기 ###
for elem in data:
  
  x = elem[0]
  list1 = [x]
  while True:
    if nextSeq(x) not in list1:
      list1.append(nextSeq(x))
      x = nextSeq(x)
    else:
      break

  y = elem[1]
  list2 = [y]
  while True:
    if nextSeq(y) not in list2:
        list2.append(nextSeq(y))
        y = nextSeq(y)
    else:
      break

  # 경우 나누기
  if list1[-1] == 1 and list2[-1] != 1:
    print(list1[0], list2[0], 0)

  elif list1[-1] != 1 and list2[-1] == 1:
    print(list1[0], list2[0], 0)
  
  else:
    pseudoAnswers = []
    for i in range(len(list1)):
      if list1[i] in list2:
        pseudoAnswer = i + list2.index(list1[i]) + 2
        pseudoAnswers.append(pseudoAnswer)

    print(list1[0], list2[0], min(pseudoAnswers))