# P P AP- --> P (P)PAP AP or P P(P)AP AP or P PPA(P) AP 
 
a = input()

# # 시간을 줄이기 위해 짧게 쳐보자.

if len(a) in [0,2,3]:
    print('NP')
    exit(0)
elif len(a) == 1:
    if a == 'P':
        print('PPAP')
        exit(0)
    else:
        print('NP')
        exit(0)
else: #len(a) >= 4 case.
    if (a[1] == 'A') or (a.endswith('PP')) or ('AA' in a) or (len(a)%3 != 1) or (a.count('A') != len(a)//3) or ('PPAP' not in a):
        print('NP')
        exit(0)
    else:
        print('PPAP')
        exit(0)
# ! 최소로 줄였을 때 아니게 되는 예시는 뭐가 있을까..? ... 
# ! 채점결과 5%에서 반례가 있음. 5% = PPAP가 없는 케이스, 
# ! 6%에서 다시 틀림. --> length로 나누었을 때도 틀리는 것으로 보아 len(a)>=4 case에서 반례가 존재함.


while 'PPAP' in a:
    a = a.replace('PPAP','P') #! 20%에서 긴게 있나..?
    print(a)
    
if a != 'P':
    print('NP')
else:
    print('PPAP')

# PPPPAP