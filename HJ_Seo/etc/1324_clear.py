from sys import stdin

N = int(stdin.readline().strip())
arr1 = tuple(map(int, stdin.readline().strip().split()))
arr2 = tuple(map(int, stdin.readline().strip().split()))

def maxleng(arr1, arr2, n):
    t = [0] * n
    
    for i in range(n):
        cnt = 0
        
        for j in range(n):
            if (arr1[i] == arr2[j]):
                if (cnt + 1 > t[j]):
                    t[j] = cnt + 1
                    
            if (arr1[i] > arr2[j]):
                if (t[j] > cnt):
                    cnt = t[j]
        # print(t)
    return max(t)
  
print(maxleng(arr1, arr2, N))

# 좋은 dp문제였다.
  