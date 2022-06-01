from itertools import permutations

year, n = map(int,input().strip().split())

maxi = ''
for i in range(n-1,-1,-1):
    maxi += str(i)

# print(maxi)
# print(int(maxi,n))

if year > int(maxi,base = n):
    print(-1)
    exit(0)

mini = '10'
for i in range(2,n):
    mini += str(i)

if year < int(mini,n):
    print(int(mini,n))
    exit(0)


permut = tuple(permutations(maxi))
# print(permut)
for i in range(len(permut)):
    num = ''.join(permut[i])
    if year >= int(num,n):
        # print(year,int(num,n))
        print(int(''.join(permut[i-1]),n))
        exit(0)