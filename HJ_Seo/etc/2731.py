# https://www.acmicpc.net/problem/2731
# ! 풀어보자!!! 난이도가 높지 않을듯.

def get_num(aim,adi):
    tmp = []
    for i in range(9):
        if i**3%10 == aim - adi:
            tmp.append(i)
    
    print(tmp)
    return tmp
    

aim = 3
adi = 0
get_num(aim,adi)