from itertools import combinations
from sys import stdin

N,K = map(int,stdin.readline().strip().split())

lst = []
for i in range(N):
    lst.append(set(map(ord,stdin.readline().strip()[4:-4])))
#각 단어에서 앞뒤 4글자를 제외한 글자들을 쪼개서 아스키코드로 변경, 겹치는 것을 제거하기 위해 set.

if K<5:
    print(0)
    exit(0)
elif K == 26:
    print(N)
    exit(0)
# 최소 알아야하는 글자 = a,n,t,i,c. 그리고 모든 글자를 알려주면 모든 단어를 알려주는 것과 같으니 두번째가 있으면 시간이 약간 줄겠지?

know = [ord('a'),ord('n'),ord('t'),ord('i'),ord('c')]
# print('know = ',know)
K -= 5
#N이 5 이상이니 5글자를 배웠다고 판단.

cnt = 0
for i in range(len(lst)):
    for j in know:
        if j in lst[i]:
            lst[i].discard(j)    # 시간 초과의 가능성1.

for i in lst:
    if len(i) == 0:
        lst.remove(i)
        cnt += 1
    elif len(i) > K:
        lst.remove(i)
        N -= 1
# lst의 글자중 know에 있는 글자들 제거.
# antic로만 만들어진 단어 제거 및 cnt에 추가.
# 정렬된 단어중 글자의 갯수가 K보다 많으면 제거. 
# print(lst)

total_lst = set()
for i in lst:
    total_lst = total_lst.union(i)  

if len(total_lst) <= K:
    print(N)
    exit(0)

pick_lst = combinations(total_lst,K)    #시간초과의 가능성2.
temp = 0
temp2 = 0
for i in pick_lst:
    for j in lst:
        if j & set(i) == j:
            temp += 1
    temp2 = max(temp2,temp)
    temp = 0

print(cnt+temp2)

# 시간 초과.. 2가지 경우중 하나, 혹은 둘 다.