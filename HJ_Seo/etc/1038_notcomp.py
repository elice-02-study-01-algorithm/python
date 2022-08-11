num = [10 for i in range(11)]

def add_num(idx):
    if num[idx] == 10:
        num[idx] = 1
    elif num[idx]<min(9,num[idx-1]-1):
        num[idx] += 1
    else:
        num[idx] = 0
        add_num(idx-1)

n = int(input())

if n>=3317:
    print(-1)
    exit(0)
elif n == 0:
    print(0)
    exit(0)

for i in range(n):
    add_num(10)
    print(num,i+1)  # 체크용 code.

while num[0] == 10:
    num.pop(0)

result = ''
for i in num:
    result += str(i)
    
print(result)


# ! ex. 100은 맨 뒤에 00때문에 감소하는 수가 아님.