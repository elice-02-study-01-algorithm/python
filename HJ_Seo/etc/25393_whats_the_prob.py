# https://www.acmicpc.net/problem/25393

# from sys import stdin

# n = int(stdin.readline().strip())
# sets = [tuple(map(int,stdin.readline().strip().split())) for _ in range(n)]

# m = int(stdin.readline().strip())

# for i in range(m):
#     a,b = map(int,stdin.readline().strip().split())
#     tmp1 = -1
#     tmp2 = 3000001
#     result = -1
#     for i in sets:
#         if i == (a,b):
#             result = 1
#             continue
        
#         elif i[0] == a:
#             tmp1 = max(tmp1,i[1])
        
#         elif i[1] == b:
#             tmp2 = min(tmp2,i[0])
            
#     if result == 1:
#         print(1)
#     elif tmp1 >= tmp2 and tmp1 >= b and a >= tmp2:
#         print(2)
#     else:
#         print(-1)


# ! 시간초과.

# from sys import stdin

# n = int(stdin.readline().strip())
# interv1 = dict()
# interv2 = dict()
# for _ in range(n):
#     a,b = map(int,stdin.readline().strip().split())
#     if a not in interv1:
#         interv1[a] = set()
#     interv1[a].add(b)
    
#     if b not in interv2:
#         interv2[b] = set()
#     interv2[b].add(a)

# m = int(stdin.readline().strip())

# for i in range(m):
#     a,b = map(int,stdin.readline().strip().split())
    
#     if a not in interv1 or b not in interv2: # a나 b가 시작에 없다면
#         print(-1)
#     else:
#         if b in interv1[a]: # [a,b]가 있는 경우.
#             print(1)
#         elif min(interv2[b]) <= a and b <= max(interv1[a]): #교집합이 존재하면.
#             print(2)
#         else:
#             print(-1)

# ! 이것도 시간 초과.

from sys import stdin,stdout

interv1 = dict() #시작 기준 dict
interv2 = dict() #끝 기준 dict

n = int(stdin.readline().rstrip())
for i in range(n):
    a,b = map(int,stdin.readline().rstrip().split())
    if a not in interv1:
        interv1[a] = {b}
    else:
        interv1[a].add(b)
    
    if b not in interv2:
        interv2[b] = {a}
    else:
        interv2[b].add(a)

m = int(stdin.readline().rstrip())

for i in range(m):
    a,b = map(int,stdin.readline().rstrip().split())
    
    try:
        if b in interv1[a]: # [a,b]가 있는 경우.
            stdout.write('1\n')
        elif min(interv2[b]) <= a and b <= max(interv1[a]): #교집합이 존재하면.
            stdout.write('2\n')
        else:
            stdout.write('-1\n')
    except:
        stdout.write('-1\n') # if a not in interv1 or b not in interv2: 대체.


# ! 아ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ 모르겠다ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ.....