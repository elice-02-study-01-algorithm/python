# from sys import stdin

# num = int(stdin.readline().strip())
# lst = list(map(int,stdin.readline().strip().split()))
# idx_set = {i for i in range(num)}

# Prime = {2}
# for i in range(3,2001): # list에 들어있는 수는 1000보다 작거나 같음.
#     for j in Prime:
#         if i%j == 0:
#             break
#     else:
#         Prime.add(i)

# def check_func(idx1,idx2,do_set,cnt):  #################################################### 최소 한개의 조합만 맞으면 됨.
#     # print(idx1,idx2,not_set)
#     if cnt == num-2 and lst[idx1]+lst[idx2] in Prime:
#         # print(lst[idx1]+lst[idx2])
#         return 1
#     elif lst[idx1]+lst[idx2] not in Prime:
#         # print(lst[idx1]+lst[idx2])
#         return 0
    
#     tmp = 0
#     tmp_set = do_set.copy()
#     tmp_set.discard(idx1)
#     tmp_set.discard(idx2)
    
#     next_fst_idx = tmp_set.pop()
#     for i in tmp_set:
#         tmp = max(tmp,check_func(next_fst_idx,i,tmp_set,cnt+2))
    
#     return tmp

# result = []
# for i in range(1,num):
#     if check_func(0,i,idx_set,0):
#         result.append(lst[i])

# if result:
#     print(*sorted(result))
# else:
#     print(-1)

# ! 시간 초과.. 20은 충분히 돌아가는데 50은 안나옴,,, 이거 역시 어떤 효율적인 제어에 대한 문제..

# from sys import stdin

# num = int(stdin.readline().strip())
# numm2 = num-2
# lst = list(map(int,stdin.readline().strip().split()))
# use_check = [False for _ in range(0,num)]

# Prime = {2}
# for i in range(3,2001): # list에 들어있는 수는 1000보다 작거나 같음.
#     for j in Prime:
#         if i%j == 0:
#             break
#     else:
#         Prime.add(i)

# not_dict = {i:set() for i in range(num)}
# do_dict = {i:set() for i in range(num)}
# def check_func(idx1,idx2,cnt):  #################################################### 최소 한개의 조합만 맞으면 됨.
#     if idx1 in not_dict[idx2]:
#         return 0
#     elif cnt == numm2 and idx1 in do_dict[idx2]:
#         return 1
#     elif lst[idx1]+lst[idx2] not in Prime:
#         not_dict[idx1].add(idx2)
#         not_dict[idx2].add(idx1)
#         return 0
#     elif cnt == numm2 and lst[idx1]+lst[idx2] in Prime:
#         do_dict[idx1].add(idx2)
#         do_dict[idx2].add(idx1)
#         return 1
    
#     use_check[idx1] = True
#     use_check[idx2] = True
    
#     tmp = 0
#     next_idx = use_check.index(False)
#     for i in range(idx1+1,num):        
#         if use_check[i] == False and i != next_idx:
#             tmp = max(tmp,check_func(next_idx,i,cnt+2))
    
#     use_check[idx1] = False
#     use_check[idx2] = False
        
#     return tmp

# result = []
# for i in range(1,num):
#     print('check용',i)
#     if check_func(0,i,0):
#         result.append(lst[i])
#     # print(do_dict)
#     # print('------')
#     # print(not_dict)

# if result:
#     print(*sorted(result))
# else:
#     print(-1)

# ! 요것도 시간 초과.

# from sys import stdin

# num = int(stdin.readline().strip())
# numm2 = num-2
# lst = list(map(int,stdin.readline().strip().split()))
# use_check = [False for _ in range(0,num)]

# Prime = {2}
# for i in range(3,2001): # list에 들어있는 수는 1000보다 작거나 같음.
#     for j in Prime:
#         if i%j == 0:
#             break
#     else:
#         Prime.add(i)

# prime_checker = {i:set() for i in range(num)}
# for i in range(num):
#     for j in range(num):
#         if lst[i] + lst[j] in Prime:
#             prime_checker[i].add(j)
#             prime_checker[j].add(i)

# def check_func(idx1,idx2,cnt):  #################################################### 최소 한개의 조합만 맞으면 됨.
#     if idx2 not in prime_checker[idx1]:
#         return 0
#     elif cnt == numm2 and idx2 in prime_checker[idx1]:
#         return 1
    
#     use_check[idx1] = True
#     use_check[idx2] = True
    
#     tmp = 0
#     next_idx = use_check.index(False)
#     for i in prime_checker[next_idx]:
#         if use_check[i] == False:
#             tmp = max(tmp,check_func(next_idx,i,cnt+2))
    
#     use_check[idx1] = False
#     use_check[idx2] = False
        
#     return tmp

# result = []
# for i in range(1,num):
#     print('check용',i)
#     if check_func(0,i,0):
#         result.append(lst[i])

# if result:
#     print(*sorted(result))
# else:
#     print(-1)

# ! 요것도 느리고.. (물론 모든 거를 치는게 아니라 겁나 빨라지긴 함..).. 50개짜리 랜덤다이스를 집어넣었을 때 특정 구간에서 느렸던 이유는 정말 계산하니라다..,,, 

# from sys import stdin

# num = int(stdin.readline().strip())
# numm2 = num-2
# lst = tuple(map(int,stdin.readline().strip().split()))
# use_check = [False for _ in range(0,num)]

# Prime = {2}
# for i in range(3,2*max(lst)): # list에 들어있는 두 수의 합은 2*max보다 작거나 같음.
#     for j in Prime:
#         if i%j == 0:
#             break
#     else:
#         Prime.add(i)

# prime_checker = {i:[False]*num for i in range(num)}
# for i in range(num):
#     for j in range(num):
#         if lst[i] + lst[j] in Prime:
#             prime_checker[j][i] = True
#             prime_checker[i][j] = True

# # print(prime_checker)
# def check_func(idx1,idx2,cnt):
#     if not prime_checker[idx1][idx2]:
#         return 0
#     elif cnt == numm2 and prime_checker[idx1][idx2]:
#         return 1
#     use_check[idx1] = True
#     use_check[idx2] = True
    
#     tmp = 0
#     next_idx = use_check.index(False)
#     use_check[next_idx] = True # ! 첫 번째 인자만 넘기면 되는 것이기 때문에 잘 돌아감.
#     for idx,TF in enumerate(prime_checker[next_idx]): # ! 여기 처리를 어떻게 하면 좋지.. 빨라지긴 했는데 뭔가 틀렸다..,,
#         if TF == True and use_check[idx] == False:
#             tmp = check_func(next_idx,idx,cnt+2)
#             if tmp:
#                 break
    
#     use_check[next_idx] = False
#     use_check[idx1] = False
#     use_check[idx2] = False
#     return tmp

# result = []
# for i in range(1,num):
#     print('check용 =',i)
#     if check_func(0,i,0):
#         result.append(lst[i])

# if result:
#     print(*sorted(result))
# else:
#     print(-1)
    
# ! 체감상 조금 더 빨라진듯.. but 느림.

# from sys import stdin
# # import time

# num = int(stdin.readline().strip())
# lst = tuple(map(int,stdin.readline().strip().split()))

# # stt_time = time.time()

# Prime = {2}
# for i in range(3,2*max(lst)): # list에 들어있는 두 수의 합은 2*max보다 작거나 같음.
#     for j in Prime:
#         if i%j == 0:
#             break
#     else:
#         Prime.add(i)
        
# # TODO :: only Rule : only use lst Index..!

# even = []
# odd = []
# for i in range(num):
#     if lst[i]%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# leng = len(even)
# lengm1 = leng-1

# if leng != len(odd):
#     print(-1)
#     exit(0)

# first = ''
# next = ''

# if lst[0]%2 == 0 :
#     first = even
#     next = odd
# else:
#     first = odd
#     next = even

# prime_checker = {i:[] for i in first}

# for i in first:
#     for j in next:
#         if lst[i]+lst[j] in Prime:
#             prime_checker[i].append(j)

# use_check = [False for _ in range(num)]  # even과 odd를 섞는 것이 결과적으로 편함..(겹치는 index가 없기 때문에.)

# def checker(init,target,cnt):
#     # global ccccc
#     # ccccc += 1
#     if cnt == lengm1 and target in prime_checker[init]:
#         return 1
    
#     use_check[init] = True
#     use_check[target] = True
    
#     for i in first:
#         if use_check[i] == False: 
#             break
    
#     for j in prime_checker[i]:
#         if use_check[j] == False:
#             tmp = checker(i,j,cnt+1)  # 재일 빠름.
#             if tmp:
#                 use_check[init] = False
#                 use_check[target] = False
#                 return 1
    
#     use_check[init] = False
#     use_check[target] = False
#     return 0

# for i in prime_checker:
#     if len(prime_checker[i]) == 0:
#         print(-1)
#         exit(0) # ! 꼼수1
#     elif len(prime_checker[i]) == 1:
#         if i == first[0]:
#             if checker(i,prime_checker[i][0],0):
#                 print(lst[prime_checker[i][0]])
#                 exit(0)
#             else:
#                 print(-1)
#                 exit(0)
#         elif use_check[prime_checker[i][0]]: # ! 꼼수2.. 두 수가 유일하게 1개의 prime 합을 가질 때.
#             print(-1)
#             exit(0)
#         else:
#             use_check[prime_checker[i][0]] = True
#             use_check[i] = True

# for i in next: # ! 꼼수3.. next의 입장에서도 살펴보기.
#     tmp = []
#     for j in first:
#         if lst[i]+lst[j] in Prime:
#             tmp.append(j)
            
#     if len(tmp) == 0:
#         print(-1)
#         exit(0)
#     elif len(tmp) == 1:
#         if tmp[0] == first[0]:
#             if checker(first[0],i,0):
#                 print(lst[i])
#                 exit(0)
#             else:
#                 print(-1)
#                 exit(0)
#         elif use_check[i] or use_check[tmp[0]]:
#             print(-1)
#             exit(0)
#         else:
#             use_check[i] = True
#             use_check[tmp[0]] = True
            
# ccccc = 0
# result = set()
# for i in prime_checker[first[0]]:
#     if not use_check[i]:
#         if checker(first[0],i,0):
#             result.add(lst[i])
    
# if result:
#     print(*sorted(result))
# else:
#     print(-1)

# # print(ccccc) # ! 함수가 몇번 도는지 체크하기 위한 변수.
# # print('interval :',time.time() - stt_time)

# ! 도대체 어디를 고쳐야 하려나..,,,

from sys import stdin
import time

num = int(stdin.readline().strip())
lst = tuple(map(int,stdin.readline().strip().split()))

stt_time = time.time()

tmp = {i for i in range(2,2000)}
Prime = set()
while True:
    if len(tmp) == 0:
        break
    x = tmp.pop()
    Prime.add(x)
    
    for i in range(x,2000,x):
        tmp.discard(i)

# TODO :: only Rule : only use lst Index..!

first = []
next = []
tmp = lst[0]%2
for i in range(num):
    if lst[i]%2 == tmp:
        first.append(i)
    else:
        next.append(i)

leng = len(first)

if leng != len(next):
    print(-1)
    exit(0)

prime_checker = {i:[] for i in first}

for i in first:
    for j in next:
        if lst[i]+lst[j] in Prime:
            prime_checker[i].append(j)

use_check = [False for _ in range(num)]  # even과 odd를 섞는 것이 결과적으로 편함..(겹치는 index가 없기 때문에.)

def checker(init,target,cnt):
    # print(lst[init],lst[target],cnt)
    # global ccccc
    # ccccc += 1
    if cnt == leng:
        return 1
    use_check[init] = True
    use_check[target] = True
    
    for i in first:
        if use_check[i] == False: 
            break
    
    for j in prime_checker[i]:
        if use_check[j] == False:
            tmp = checker(i,j,cnt+1)  # 재일 빠름.
            if tmp:
                use_check[init] = False
                use_check[target] = False
                return 1
    
    use_check[init] = False
    use_check[target] = False
    return 0

for i in prime_checker:
    if len(prime_checker[i]) == 0:
        print(-1)
        exit(0) # ! 꼼수1.. O(max(25))
        
# ccccc = 0
result = set()
for i in prime_checker[first[0]]:
    if checker(first[0],i,1):
        result.add(lst[i])
    
if result:
    print(*sorted(result))
else:
    print(-1)

# print(ccccc) # ! 함수가 몇번 도는지 체크하기 위한 변수.
print('interval1 :',time.time() - stt_time)

###### !!! 도저히 모르겠다.. 이분탐색 + 재귀로써 최대한의 효율을 뽑은 것 같은데..   index와 real을 섞어보면..?

### ! 아래쪽은 비교군.... max_flow_min_cut Thm을 이용한 풀이같다.
import time
import sys
import collections
import math

stt_time = time.time()

VMAX = 52
SOURCE = 50
SINK = 51
NN = 2000
 
primes = [True] * (NN)
primes[1] = False
for i in range(2, NN):
  if primes[i]:
    for j in range(i*2, NN, i):
      primes[j] = False
 
def isPrime(val):
  return primes[val]
 
def bfs(flow, capacity, source, sink):
  parent = [-1] * VMAX
  q = collections.deque([source])
  parent[source] = source
  while len(q) != 0:
    item = q.popleft()
    for i in range(VMAX):
      if parent[i] == -1 and capacity[item][i] - flow[item][i]:
        q.append(i)
        parent[i] = item
  return parent
 
def maxFlow(capacity, source, sink, flow):
  rst = 0
  while True:
    parent = bfs(flow, capacity, source, sink)
    if parent[sink] == -1:
      return rst
    #minimum
    node = sink
    m = math.inf
    while node != source:
      m = min(m, capacity[parent[node]][node] - flow[parent[node]][node])
      node = parent[node]
    #add
    rst += m
    node = sink
    while node != source:
      flow[parent[node]][node] += m
      flow[node][parent[node]] -= m
      node = parent[node]
 
def solve():
  n = int(sys.stdin.readline().rstrip())
  arr = list(map(int, sys.stdin.readline().rstrip().split()))
  even = []
  odd = []
  for i in range(n):
    if arr[i] % 2 == 0:
      even.append(i)
    else:
      odd.append(i)
  # build graph
  graph = [[0] * VMAX for _ in range(VMAX)]
  for i in even:
    graph[SOURCE][i] = 1
  for i in odd:
    graph[i][SINK] = 1
  for i in even:
    for j in odd:
      if isPrime(arr[i] + arr[j]):
        graph[i][j] = 1
  rst = []
  while True:
    flow = [[0] * VMAX for _ in range(VMAX)]
    val = maxFlow(graph, SOURCE, SINK, flow)
    if val == n // 2:
      if arr[0] % 2 == 0: # even 
        for i in odd:
          if flow[0][i] == 1:
            rst.append(arr[i])
            graph[0][i] = 0
      else:
        for i in even:
          if flow[i][0] == 1:
            rst.append(arr[i])
            graph[i][0] = 0
    else:
      break
  if len(rst) == 0:
    print(-1)
  else:
    rst.sort()
    for item in rst:
      print(item, end = ' ')
    print("")
 
solve()
print('interval2 :',time.time()-stt_time)

'''
50
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50
--> 2 4 6 10 12 16 18 22 28 30 36 40 42 46(358 round)
10
34 39 32 4 9 35 14 17 1 4
--> 9 39(16 round)
18
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
--> 2 4 6 10 12 16 18(82 round)
8
34 39 32 4 9 35 14 17
--> 9 39(10 round)
20
941 902 873 841 948 851 945 854 815 898 806 826 976 878 861 919 926 901 875 864
--> 806 926(35 round)
38
757 97 337 221 971 496 138 12 5 342 275 159 467 523 270 118 273 846 564 597 698 931 200 745 205 914 172 372 339 826 26 777 351 436 180 1000 487 218
--> 12 172 180 372 436 564 826(100421 round)
30
937 824 721 524 517 722 43 251 379 611 993 256 717 970 462 571 789 696 96 630 94 132 233 699 980 695 854 959 572 290
--> 94 96 132 256 462 970(1387 round)
6
11 1 4 7 10 12
--> 12(3 round)
50
972 492 840 160 158 550 390 508 726 206 632 442 194 958 434 978 128 474 832 994 850 176 430 212 582 673 415 417 659 273 575 475 909 977 153 323 337 33 515 985 793 325 495 873 533 905 53 343 111 179
--> 179 325 475 515 905 977 (386 round)
50
846 286 682 952 566 138 544 678 478 10 128 574 914 786 28 94 768 470 668 870 284 954 242 368 8 179 545 5 537 91 451 567 473 791 597 417 17 39 321 793 627 841 609 741 963 107 461 401 349 463
--> 17 91 107 451 461 473 791 (76542 round)
50
53 641 733 429 995 627 945 127 979 989 543 521 805 201 345 611 91 211 931 783 363 913 269 77 401 738 668 440 324 170 212 42 514 534 232 308 558 598 724 286 304 160 120 698 962 130 834 760 832 428
--> 120 170 534 698 834(11860 round)
50
350 7 606 761 464 799 372 551 668 889 628 353 916 611 868 779 332 599 644 59 638 469 844 967 630 871 950 909 708 295 824 711 962 259 786 753 480 213 670 895 490 411 932 543 120 179 164 145 352 725
--> 213 411 711 753 779 909
'''