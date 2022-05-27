# 메모리 38652kb, 시간 80ms 
# 너비우선탐색 방식
a = int(input())
lst = [a]
v = [0] * (10 ** 6 + 1) # 문제에서 주어진 최대 숫자로 배열 생성
v[a] = 1 
temp = 0

while v[1] == 0: # 1을 방문할 때까지
    new_lst = []
    
    for num in lst:
        v[num] = 1 # 방문처리
        if num % 3 == 0 and v[num // 3] == 0:
            v[num // 3] = 1
            new_lst.append(num // 3) # for문 안에서는 pop을 하면 문제가 생기기 때문에 리스트를 하나 더 만들어서 필요한 숫자만 append
        if num % 2 == 0 and v[num // 2] == 0:
            v[num // 2] = 1
            new_lst.append(num // 2)
        if v[num - 1] == 0:
            v[num - 1] = 1
            new_lst.append(num - 1) 
            
    temp += 1
    lst = new_lst
    
print(temp)