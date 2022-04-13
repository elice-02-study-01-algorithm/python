#백준 1912와 동일.

def max_sum(data) :
    maxSum = []
    final_max = data[0]
    maxSum.append(final_max)

    for i in range(1,len(data)):
        maxSum.append(max(maxSum[i-1],0)+data[i])
        if final_max <maxSum[i]:
            final_max = maxSum[i]
    
    return final_max

n = input()
data = list(map(int,input().strip().split()))

print(max_sum(data))