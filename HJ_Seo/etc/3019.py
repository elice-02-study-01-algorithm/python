from sys import stdin

width , num = map(int,stdin.readline().strip().split())
arr = tuple(map(int,stdin.readline().strip().split()))

shapes = []
if num == 1:
    shapes = [[0],[0,0,0,0]]
elif num == 2:
    shapes = [[0,0]]
elif num == 3:
    shapes = [[0,0,1],[1,0]]
elif num == 4:
    shapes = [[1,0,0],[0,1]]
elif num == 5:
    shapes = [[0,0,0],[0,1],[1,0,1],[1,0]]
elif num == 6:
    shapes = [[0,0,0],[0,0],[0,1,1],[2,0]]
elif num == 7:
    shapes = [[0,0,0],[0,2],[1,1,0],[0,0]]

result = 0
while len(shapes) != 0:
    shape = shapes.pop()
    if len(shape) == 1:
        result += len(arr)
        continue
    
    for i in range(len(arr)-len(shape)+1):
        temp = [0 for _ in range(len(shape))]
        for k in range(len(shape)):
            temp[k] = arr[i+k] - shape[k]
        
        if min(temp) == max(temp):
            result += 1
            
        # print(temp)

print(result)

#! 대강 주석과 빈 줄등을 지운 결과 숏코딩 43등!!!ㅋㅋㅋㅋ