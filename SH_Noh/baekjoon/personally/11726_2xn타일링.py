from sys import stdin

n = int(stdin.readline())

case = [1, 1] # 각각 n이 0과 1일 때
for i in range(2, n + 1): # 2부터 n일 때까지
    case.append((case[i-1] + case[i-2]) % 10007)
print(case[n])