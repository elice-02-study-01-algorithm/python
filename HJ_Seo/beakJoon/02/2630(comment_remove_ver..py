#2630 색종이 만들기
def div_to_quarter(square_list):
    if len(square_list) == 1:
        return -1
    if len(square_list) not in [2,4,8,16,32,64,128]:
        return -2
    
    half = len(square_list)//2

    A_high = square_list[:half]
    A_low = square_list[half:]

    A1=[]
    A2=[]
    A3=[]
    A4=[]
    
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
white = 0

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
