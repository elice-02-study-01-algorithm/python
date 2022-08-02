[0,1,2,3]


'''
X

1

1+1
2

1+1+1
2+1
3

1+1+1+1
2+1+1
2+2
3+1

1+1+1+1+1
2+1+1+1
2+2+1
3+1+1
3+2

1*6
2+1*4
2*2+1*2
2*3
3+1*3
3+2+1*2
3+3

3이 있는 갯수로 count.
'''

# n = int(input())
# three_num = n//3
# three_div = n%3
# two_num = []
# for i in range(n+1):
#     two_num.append(int(i)//2+1)
    

# '''
# 3*3.. 1.. 1
# 3*2.. 4.. 3
# 3*1.. 7.. 4
# 3*0.. 10.. 6

# sum = 14
# '''
# result = 0
# for i in range(three_div,n+1,3):
#     result += two_num[i]
#     # print(result)

# print(result)


from sys import stdin

case = int(stdin.readline().strip())

two_num = []
three_num = 0
three_div = 0
for _ in range(case):
    num = int(stdin.readline().strip())
    three_num = num//3 + 1
    three_div = num%3
    if len(two_num)<num+1:
        for i in range(len(two_num),num+1):
            two_num.append(i//2+1)

    result = 0
    for i in range(three_div,num+1,3):
        result += two_num[i]
    
    print(result)