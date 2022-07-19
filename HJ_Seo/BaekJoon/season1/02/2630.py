'''
input : 
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
========
output : (0사각형(white), 1사각형(blue).)
9
7
'''

def div_to_quarter(square_list):
    if len(square_list) == 1:
        return -1 #못나누기 때문에 버그메시지로 쓰일 -1 출력.
    if len(square_list) not in [2,4,8,16,32,64,128]:
        return -2 #예제에 없을꺼니까 나오면 이상한거.
    
    half = len(square_list)//2

    A_high = square_list[:half]
    A_low = square_list[half:]

    A1=[]   # 각각 1,2,3,4분면이라 생각하자.
    A2=[]   #  [[1,2],[3,4]] 를 넣었을 때 차례대로 2,1,3,4가 들어가야 함.
    A3=[]   # done.
    A4=[]   #
    
    for row in A_high:
        A1.append(row[half:])
        A2.append(row[:half])

    for row in A_low:
        A3.append(row[:half])
        A4.append(row[half:])

    return [A1,A2,A3,A4]

square_length = int(input())
square = [list(map(int,input().strip().split())) for _ in range(square_length)]
square_list = [square]
blue = 0
white = 0  #리턴해줄 두 값.

while len(square_list) != 0:
    check_one = square_list.pop()

    if sum(sum(check_one,[]))==len(check_one)**2:
        blue += 1
    elif sum(sum(check_one,[]))==0:
        white += 1
    else:
        square_list += div_to_quarter(check_one)

print(white)
print(blue)


# 한큐에 성공!