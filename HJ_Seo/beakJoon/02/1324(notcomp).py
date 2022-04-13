#이 코드의 문제점... 부분수열이 단조증가가 아니어도 카운트한다는 것..!..
def same_seq_distance(s1, s2):

    m = len(s1)
    n = len(s2)
        
    L = [[None]*(n+1) for i in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i ==0 or j == 0:
                L[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i][j-1],L[i-1][j])
    for k in L:
        print(k)
    print(L[i][j])
    # print(max(sum(L,[])))

n = input()
s1 = list(map(int,input().strip().split()))
s2 = list(map(int,input().strip().split()))

same_seq_distance(s1, s2)   

#재일 긴 증가수열.. from s1

longest = [[None]*len(s1) for _ in range(len(s1))]
for i in range(len(s1)):
    longest[i][i] = [s1[i]]

for i in range(len(s1)):
    for j in range(i+1,len(s1)):
        if longest[-1] <= s1[j]:
            longest = max(longest,s1[i:j],key = lambda x:len(x))




# def same_seq_distance(s1, s2):

#     n = len(s1)
        
#     L = [[[]]*(n+1) for i in range(n+1)]
#     for i in range(1,n+1):
#         L[i][i].append(s1[i-1])

#     for k in L:
#         print(k)

#     for i in range(-n-2,-1,-1):
#         for j in range(i+1,n):
#             if 
#     # print(max(sum(L,[])))


# n = input()
# s1 = list(map(int,input().strip().split()))
# s2 = list(map(int,input().strip().split()))

# same_seq_distance(s1, s2)   