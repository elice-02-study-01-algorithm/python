
'''
100..
1~100에서.. 50~100 - 51
1~23에서.. 11~23 - 13
1~4에서.. 2~4 - 3

1000..
500~1000 - 501
124~248 - 125
30~60 - 31
6~13 - 8
1 - 1
999..

'''
# print(124*2+2)

# n = int(input())
# num = 0
# not_use_max = 0
# # print(n//3*2+1)
# while n > 1:
#     if n%2 == 0:
#         num += n//2 + 1
#     else:
#         num += n//2 + 2
    
#     not_use_max = n//2 - 1
#     # print(not_use_max)
#     # break
#     n = not_use_max//2 - 1
#     print(n)
#     break
    
# print(num)

def calc(n):
    if n<4:
        return n
    elif n<10:
        return ((n+1)//2+1)
    else:
        return calc((n//2-3)//2)+(n+1)//2+1
        
print(calc(int(input())))
# print(calc(10000000000))
# print(calc(1000))
# print(calc(10000))
'''
10000000000
6666666667
if n < 4:
    print(n)
elif n<10:
    print((n+1)//2+1)
else:
    print(P((n//2-1)//2)+(n+1)//2+1)  --> (n//2-1)//2 요 숫자 이상쓰..

1 --> 1.. 1
2 --> 12.. 2 
3 --> 123.. 3
4 --> 234.. 3 
5 --> 2345.. 4
6 --> 3456.. 4
7 --> 34567.. 5
8 --> 45678.. 5
9 --> 456789.. 6
10 --> 1 5~10.. 7 == P(1)+(10+1)//2+1
11 --> 1 5~11.. 8 == P(1)+(11+1)//2+1
12 --> 1 6~12.. 8 == P(1)+(12+1)//2+1
13 --> 1 6~13.. 9 == P(1)+(13+1)//2+1
14 --> 12 7~14.. 10 == P(2)
15 --> 12 7~15.. 11
16 --> 12 8~16.. 11
17 --> 12 8~17.. 12
18 --> 123 9~18.. 13 P(3)
19 --> 123 9~19.. 14 
20 --> 123 10~20.. 14
21 --> 123 10~21.. 15
22 --> 234 11~22.. 15
24 --> 234 12~24.. 16
 
 
 1 3 5 7 9 11 13 15 17 19 21 23 - 12
 4 8 12 16 20 24(xxx)
 2(6x) - 1
 10(22x) 14 18 - 3 
'''