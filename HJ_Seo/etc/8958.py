# b2 OX퀴즈 

n = int(input())

for _ in range(n):
    result = 0
    arr = input().split('X')
    
    for i in arr:
        result += ( len(i) * (len(i)+1) ) // 2
    
    print(result)
    