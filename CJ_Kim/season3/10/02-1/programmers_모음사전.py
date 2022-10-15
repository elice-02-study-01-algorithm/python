def solution(word):
    answer = 0
    vowelBox = ['X', 'A', 'E', 'I', 'O', 'U']
    # 각 자리 수가 고정됐을 떄 가질 수 있는 개수
    # ex. AXXXX -> 781개, EIXXX -> 156개
    standardNum = [781, 156, 31, 6]
    # 글자 5개로 맞춰주기
    while len(word)<5:
        word+='X'
    for charIndex in range(5):
        if charIndex == 4:
            answer += vowelBox.index(word[charIndex])
            break
        answer+=standardNum[charIndex]*(vowelBox.index(word[charIndex])-1)
        answer += 1
        if word[charIndex+1]=='X':
            break
    
    return answer

print(solution("A"))
print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))
'''
A0000
AA000
AAA00 -> 31 

AAA
AAAA0*6
AAAE0*6
AAAI0*6
AAAO0*6
AAAU0*6
+ 1

AAA00*31
AAE00*31
AAI00*31
AAO00*31
AAU00*31
=> AA000 = 1(AA) + 155

AA000*156
AE000*156 
AI000*156
AO000*156
AU000*156

A로 시작: 1(A) + 156*5 = 1 ~ 781
AAAA0 : 4(AAAA)~9(AAAAU) -> 6개
AAAAE : 1+1+1+1+2
AAAE : 1+1+1+6+1
E로 시작: 1 + 156*5 = 782~1562
E: 782번째
EA 5 5 6 : 156 / 783 ~ 938
EE 5 5 6 : 156 / 939 ~ 1094
EI:  1095번째
EIA 5 6 : 31 / 1096 ~ 1126
EIE 5 6 : 31 / 1127 ~ 1157
EII 5 6 : 31 / 1158 ~ 1188
EIO : ((1+781)+312+1)+93 + 1 = 1189
I: 1563번째
...

'''