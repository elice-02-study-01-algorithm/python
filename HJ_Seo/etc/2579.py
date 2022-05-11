'''
P(i) : i번째 계단을 오를 때 최대합.
Q(i) : i번째 계단을 오를 때 직전에 두칸을 점프한 최대합.
R(i) : i번째 계단을 오를 떄 직전에 연속으로 밝고 올라온 최대합.
==> P = max(Q,R)
Q(n) = P(n-2) + stare[n]
R(n) = Q(n-1)+stare[n] = P(n-3)+stare(n-1)+stare[n]

P(n) = max(Q(n),R(n)) = max(P(n-2),P(n-3)+stare(n-1)) + stare[n]


'''
def max_sum(lst):
    if len(lst) <= 2:
        return sum(lst)

    height = len(lst)    
    stare_sum = [0,lst[0],lst[0]+lst[1]]

    for i in range(3,height+1):
        maxone = max(stare_sum[i-2],stare_sum[i-3]+lst[i-2]) + lst[i-1]
        stare_sum.append(maxone)

    return stare_sum[-1]

n = int(input())

stare = []
for i in range(n):
    stare.append(int(input()))

print(max_sum(stare))