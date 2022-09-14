from sys import stdin
input = stdin.readline

# A B A+B A+2B 2A+3B "3A+5B" 5A+8B 8A+13B
# 2 7 9   16   25     41

day, dduck = map(int, input().split())
fibo = [1, 1] + [0 for _ in range(day - 3)]
for n in range(2, day - 1):
    fibo[n] = fibo[n - 1] + fibo[n - 2]

# day날의 dduck 개수 = (fibo[-2]A + fibo[-1]B)개
a = fibo[-2]
b = fibo[-1]
A = 1
for A in range(1, dduck):
    if (dduck - a * A) % b == 0:
        B = (dduck - a * A) // b
        break
    
print(A)
print(B)
