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
'''
설명.
(위의 주석들은 아이디어를 떠올리기 위한 결과입니다.)

1개의 아이디어를 생각해서 리스트를 이용해서 풀었습니다.(다시보니 리스트를 하나 더 만들어서 저장해놨으면 훨씬 빨리 끝났겠네요.)
아이디어는 '각 숫자를 나타낼 때 3이 몇개가 들어가는지?' 입니다. 
예를 들어 7에 3이 하나 들어가있는 경우를 따져보면 1+1+1+1,2+1+1,2+2로 2가 몇개 들어갈 수 있는지 따지는 문제와 동일한 문제가 됩니다.
그리고 이 숫자는 4를 1과 2만으로 만드는 경우의 수와 동일하고, 이것들을 리스트에 저장한 후 iterator를 이용해서 3 단위 차이의 합을 구했습니다.
'''

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