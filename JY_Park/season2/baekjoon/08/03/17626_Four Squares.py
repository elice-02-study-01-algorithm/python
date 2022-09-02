# for i in range(int(n ** (1/2)),1,-1):
#     if i ** 2 == n:
#         count += 1
#         n -= i ** 2

# 아이디어 1 : 제곱으로 만들어나가다가 안되면 백트래킹

def dfs():
    n = int(input())

    if (n ** (1/2)) % 1 == 0:
        return 1

    for i in range(int(n ** (1/2)),0,-1):
        if n < i ** 2:
            break
        # 원래는 n을 직접 뺐는데 몇 개인지만 체크해도 되니깐 이렇게 변경
        if ((n - i ** 2) ** (1/2)) % 1 == 0:
            return 2
    for i in range(int(n ** (1/2)),0,-1):
        if n < i ** 2:
            break
        for j in range(int((n - i ** 2) ** (1/2)),0,-1):
            if n < i ** 2 + j ** 2:
                break
            if ((n - i ** 2 - j ** 2) ** (1/2)) % 1 == 0:
                return 3
    return 4

# n = int(input())
print(dfs())

'''
1. 처음에는 count로 재귀 돌 때마다 +1 하고 백트래킹하려고 했는데
꼬였음. 
-> 그리고 문제를 다시 읽어보니 라그랑주는 자연수 4 이하의 
제곱수의 합으로 표현할 수 있다는 것을 봄.
그리고 n을 자꾸 빼줬더니 값 이상
'''


# def dfs():
#     if len(s) == m:
#         print(' '.join(map(str, s)))
#         return
    
#     for i in range(1,n+1):
#         if i not in s:
#             s.append(i)
#             dfs()
#             s.pop()

# n, m = map(int, input().split())
# s = []

# dfs()