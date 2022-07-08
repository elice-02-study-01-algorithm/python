from sys import stdin

n, need = map(int,stdin.readline().strip().split())

lopes = [int(stdin.readline().strip()) for _ in range(n)]

stt = max(lopes)

def cnt_sum(lopes,n,leng):
    sum = 0
    for i in range(n):
        sum += lopes[i]//leng
    
    return sum

leng_sum = 1
while need > leng_sum:
    stt = stt//2
    leng_sum = cnt_sum(lopes,n,stt)

temp = stt//2
while True:
    leng_sum = cnt_sum(lopes,n,stt+temp)
    if need > leng_sum:
        temp = temp//2
        # print(temp)
    else:
        stt += temp
    
    if temp == 0:
        break

print(stt)