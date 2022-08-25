n = int(input())
# 제곱을 저장
squares = [i * i for i in range(1, 224)]

# 제곱안에 있으면 찾았다!
if n in squares:
    print(1)
    exit()

# 26
# 1 ~ 5
# 26 - 1 = 25 => 1*1 + 5*5

for i in range(1, int(n**0.5) + 1):
    if n - i*i in squares:
        print(2)
        exit()

for i in range(1, int(n**0.5) + 1):
    for j in range(1, int(n**0.5) + 1):
        if n - i*i - j*j in squares:
            print(3)
            exit()
print(4)
