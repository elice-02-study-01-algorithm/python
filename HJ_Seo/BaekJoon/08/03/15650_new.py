# https://www.acmicpc.net/problem/15650
# 이미 풀었던게 있던데 괄목상대라는 것이 무슨 말인지 알 것 같더군요..ㅎㅎ..(왜 파일로 저장을 안해놨는지 모르겠음..) 
# 요건 새로 푼 풀이입니다.

def change_next(lst,maxi):
    if lst[-1] < maxi:
        lst[-1] += 1
        return lst
    else:
        lst = change_next(lst[:-1],maxi-1)
        lst.append(lst[-1]+1)
        return lst

num,leng = map(int,input().split())

lst = [i for i in range(1,leng+1)]
last = [i for i in range(num+1-leng,num+1)]

while True:
    print(*lst)
    
    if lst == last:
        break
    
    lst = change_next(lst,num)
