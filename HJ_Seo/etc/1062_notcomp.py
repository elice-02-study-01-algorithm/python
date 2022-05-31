from itertools import combinations
from sys import stdin

N,K = map(int,stdin.readline().strip().split())

lst = [set(map(ord,stdin.readline().strip()[4:-4])) for _ in range(N)]
#각 단어에서 앞뒤 4글자를 제외한 글자들을 쪼개서 아스키코드로 변경, 겹치는 것을 제거하기 위해 set.

if K<5:
    print(0)
    exit(0)
elif K == 26:
    print(N)
    exit(0)
# 최소 알아야하는 글자 = a,n,t,i,c. 그리고 모든 글자를 알려주면 모든 단어를 알려주는 것과 같으니 두번째가 있으면 시간이 약간 줄겠지?

know = {ord('a'),ord('n'),ord('t'),ord('i'),ord('c')}
# alp_except_know = set([i for i in range(97,123)]) #ord('a') = 97, ord('z') = 122
# for i in know:
#     alp_except_know.remove(i)
    
# print('know = ',know)
K -= 5
#know가 5 이상이니 5글자를 배웠다고 판단.

for i in range(len(lst)):
    lst[i] = lst[i] - know

cnt = lst.count(set())

for i in lst:
    if len(i) == 0:
        lst.remove(i)
    elif len(i) > K:
        lst.remove(i)

# lst의 글자중 know에 있는 글자들 제거.
# antic로만 만들어진 단어 제거 및 cnt에 추가.
# 정렬된 단어중 글자의 갯수가 K보다 많으면 제거. 검사케이스 줄이기.
# print(lst)

total_lst = set().union(*lst)
# check = combinations(total_lst,K)

result = 0
for i in combinations(total_lst,K):
    result = max(result, len(['' for subset in lst if subset & set(i) == subset]))
    
print(result+cnt)

# print(lst) 
# print(total_lst)

# if len(total_lst) <= K:
#     print(N)
#     exit(0)


# n = len(total_lst) # 원소의 개수
# result_list = [] # 생성된 부분 수열 저장
# for i in range(1<<n): # 부분 수열 개수
#     subset = set() # 부분수열 담기 위함
#     for j in range(n): # 원소의 수만큼 비트를 비교함
#         if i & (1 << j):
#             subset.add(total_lst[j]) # 부분 수열 만들기
#             if len(subset) == K:
#                 break
#     if subset not in result_list:
#         result_list.append(set(subset))

# print(result_list)

# print(lst)
# print(result_list[10])

# print(lst.count(key = lambda x: x & result_list[10] == x))

# pick_lst = combinations(total_lst,K)    #시간초과의 가능성2.
# temp = 0
# temp2 = 0
# for i in pick_lst:
#     for j in lst:
#         if j & set(i) == j:
#             temp += 1
#     temp2 = max(temp2,temp)
#     temp = 0

# print(cnt+temp2)

# 시간 초과.. 2가지 경우중 하나, 혹은 둘 다.

