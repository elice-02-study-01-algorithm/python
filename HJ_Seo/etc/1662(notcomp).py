# print(len("11777777777777777777777777"))
# 새로운 문자열? ( -- 어차피 짧아서...)

string = input()

small = [] #( 위치.
new_str = ""
for i in range(len(string)):
    new_str += string[i]
    
    if string[i] == "(":
        small.append(i)
        
    elif string[i] == ")":  #elif를 쓴 이유는 if를 썼을 때 문장보다 메모리 처리속도가 좀 더 적게 들기 때문.(매우 조금 효율적)
        lastone = small.pop() #마지막 (의 위치
        mull = int(string[lastone-1])  #마지막( 바로 앞의 정수. done..
        # print('제거되는 곳..',new_str[lastone-1:])
        temp = new_str[lastone+1:-1] #괄호 안쪽의 숫자
        new_str = new_str[:lastone-1] # (바로 앞의 곱셈수까지 제거
        # print('제거한 후 남은곳..',new_str)
        # print('nul과 temp : ',mull,'/',temp)
        # print('new = ',new_str)
        
        new_str += temp*mull
        
    # print(new_str)
print(len(new_str))
#백준(1662번)에서는 메모리 초과...ㅋㅋㅋㅋㅋㅋㅋㅋ     https://www.acmicpc.net/problem/1662


# 1
# 11
# 11(
# 11(18
# ...
# 11(18(72(
# 11(18(72(7
# 11(18(72(7)
#  - 11(18(777
# 11(18(777)
#  - 11(1777777777777777777777777
# 11(1777777777777777777777777)
#  - 11777777777777777777777777
#  ...
# ~~ string end & cnt.