# P P AP- --> P (P)PAP AP or P P(P)AP AP or P PPA(P) AP 


# # 시간을 줄이기 위해 짧게 쳐보자.

# a = input()

# if len(a) in [0,2,3]:
#     print('NP')
#     exit(0)
# elif len(a) == 1:
#     if a == 'P':
#         print('PPAP')
#         exit(0)
#     else:
#         print('NP')
#         exit(0)
# else: #len(a) >= 4 case.
#     if (a[1] == 'A') or (a.endswith('PP')) or ('AA' in a) or (len(a)%3 != 1) or (a.count('A') != len(a)//3) or ('PPAP' not in a):
#         print('NP')
#         exit(0)
#     else:
#         print('PPAP')
#         exit(0)

# ! 최소로 줄였을 때 아니게 되는 예시는 뭐가 있을까..? ... 
# ! 채점결과 5%에서 반례가 있음. 5% = PPAP가 없는 케이스, 
# ! 6%에서 다시 틀림. --> length로 나누었을 때도 틀리는 것으로 보아 len(a)>=4 case에서 반례가 존재함.
# ! 시간이 없기 때문에 pass..

# from sys import stdin
# a = stdin.readline().strip()

# if len(a) == 1:
#     if a == 'P':
#         print("PPAP")
#     else:
#         print("NP")
#     exit(0)

# b = ''
# for i in a:
#     b += i
#     if b.endswith('PPAP'):
#         b = b[:-3]
#     # print('b = ',b)

# if b == 'P':
#     print('PPAP')
# else:
#     print("NP")

# ! 시간 초과.(짐작했다.)

from sys import stdin

a = stdin.readline().strip()

a2 = []
for i in a:
    a2.append(i)
    if a2[-4:] == ['P','P','A','P']:
        a2.pop()
        a2.pop()
        a2.pop()
            
if a2 == ['P']:
    print('PPAP')
else:
    print('NP')    

# PPPPAP