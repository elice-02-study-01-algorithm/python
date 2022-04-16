def makeOne(x):
    global count, path
    for i in range(2, x+1):
        count[i] = count[i-1] + 1
        path[i] = i-1
        if i % 2 == 0 and count[i//2] + 1 < count[i]:
            count[i] = count[i//2] + 1
            path[i] = i//2
        if i % 3 == 0 and count[i//3] + 1 < count[i]:
            count[i] = count[i//3] + 1
            path[i] = i//3

def getpath(x):
    global path
    current = x
    while current != 0:
        print(current, end=' ')
        current = path[current]

N = int(input())
count = [0 for _ in range(N+1)]
path = [0 for _ in range(N+1)]
makeOne(N)
print(count[N])
getpath(N)