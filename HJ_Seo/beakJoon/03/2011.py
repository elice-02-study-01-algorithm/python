'''
잘못된 문자열의 케이스.
n = '', '0 ~~~'
'k0' in n where k>2


'''

n = input()

def checker(n):
    if n=='':
        return 0
    elif n.startswith('10') or n.startswith('20'):
        return 1
    elif len(n)==1:
        if n[0] == '0':
            return 0
        elif n[0] != '0':
            return 1

    # for i in ['30','40','50','60','70','80','90','00']:
    #     if i in n:
    #         return 0 #바로 아래가 함의할 수 있음.

    for i in range(3,10):
        if n.startswith(str(i)):
            return checker(n[1:])

    for i in ['1','2']:
        if n.startswith(i):
            return checker(n[1:]) + checker(n[2:])

print(checker(n))


# 1111111111 --> 89 ???
# 25114 --> 6
# n 바로 뒤에 1 혹은 2가 붙는 경우.
# 점화식으로 하는 것은 상당히 난해... 12340169 이런 것이 있을 가능성이 있고,
# 0169 바로 앞에 1혹은 2가 들어갈 가능성이 있기 때문.
# 0 1 1 2 3 5 8 13 21 34 55..?
# 0 1 2 3 4 5 6 7  8  9  10
# 11 11 11 11 11
# 1 1 1 1 1 1 1 1 1
# 1 2 3 5 8 13 21 34 55 89..?

