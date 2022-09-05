
# 아이디어: 출력값은 무조건 4 이하이다.
# == 1이 아니고, 2 아니고, 3도 아니면 4이다.
number = int(input())

# 50000 이하의 제곱인 수 
squareList = [i**2 for i in range(1, 224)]

# 입력받은 수보다 작은 제곱수의 리스트
rangeList = list(filter(lambda x: x<number, squareList))

# 입력받은 수 자체가 제곱수라면 바로 1 출력하기
if number**(1/2) == int(number**(1/2)):
    print(1)
    exit()

# 1이 아니면 2인지 판단하기
for squareNum in filter(lambda x:x<number, rangeList):
    if (number-squareNum)**(1/2) == int((number-squareNum)**(1/2)):
        print(2)
        exit()

for squareNum01 in filter(lambda x: x<number, rangeList):
    for squareNum02 in filter(lambda x:x<(number-squareNum01), rangeList):
        if (number-squareNum01-squareNum02)**(1/2) == int((number-squareNum01-squareNum02)**(1/2)):
            print(3)
            exit()

print(4)