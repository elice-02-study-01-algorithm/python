from sys import stdin

N,M = map(int,stdin.readline().rstrip().split())

result = 'Yes'
for _ in range(2*M):
    books = list(map(int,stdin.readline().rstrip().split()))
    if books != sorted(books,reverse=True):
        result = 'No'
        break
    
print(result)