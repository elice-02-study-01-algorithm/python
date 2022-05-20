# ! 주석 달기

from sys import stdin

n = int(stdin.readline().strip())
a,b = list(map(int,stdin.readline().strip().split()))
m = int(stdin.readline().strip())

root_dict = {}

for i in range(m):
    par,chi = map(int,stdin.readline().strip().split())
    if par in root_dict.keys():
        root_dict[par].append(chi)
    else:
        root_dict[par] = [chi]

# root_dict : 부모를 key로 가지는 directed forest 생성.
# print(root_dict)

def search_met(a,b,root_dict):
    a_anc = [a]
    b_anc = [b]
    # a와 b의 조상들을 나열할 리스트.. ex. a_anc[n] 은 a의 n세대 위, a_anc[-1], b_anc[-1] = 트리(들)의 root
    
    
    while a_anc[-1] in sum(root_dict.values(),[]):
        for i in root_dict.keys():
            if a_anc[-1] in root_dict[i]:
                a_anc.append(i)
                break
            
    while b_anc[-1] in sum(root_dict.values(),[]):
        for i in root_dict.keys():
            if b_anc[-1] in root_dict[i]:
                b_anc.append(i)
                break
    # while문의 조건이 성립할 수 있는 이유는 rooted 트리의 root가 어떤 vertex의 child가 되지 않기 때문.

    if len(set(a_anc) & set(b_anc)) == 0:
        return -1
    else:
        for i in a_anc:
            if i in b_anc:
                return a_anc.index(i) + b_anc.index(i)
    # 판별기. 만약 a를 포함한 tree와 b를 포함한 트리가 다르다면 root 역시 다르기 때문에 set으로 겹치는 원소가 0, return -1.
    # 아닌 경우, a의 조상을 차례대로 올라감, 이때 i가 b의 조상이 된다면 a와 b의 가장 낮은 계층의 공통조상을 찾을 수 있고, index를 통해 촌수를 알 수 있게 됨.
    
print(search_met(a,b,root_dict))

