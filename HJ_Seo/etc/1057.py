# def div_num(num):
#     if num%2 == 0:
#         return num//2
#     return num//2 + 1

# N,kim,lim = map(int,input().split())

# if kim > lim:
#     kim,lim = lim,kim

# cnt = 1
# while True:
#     if (kim+1)//2 == (lim+1)//2:
#         print(cnt)
#         break
#     # print(kim,lim)
#     kim = div_num(kim)
#     lim = div_num(lim)
#     cnt += 1

N,kim,lim = map(int,input().split())

cnt = 1
while True:
    if (kim+1)//2 == (lim+1)//2:
        print(cnt)
        break
        
    kim = (kim+1)//2
    lim = (lim+1)//2
    cnt += 1

'''
20 31 -- 1
10 16 -- 2
5 8 -- 3
3 4 -- 4
'''

'''
1000 35000 -- 1
500 17500 -- 2
250 8750 -- 3
125 4375 -- 4
63 2188 -- 5
32 1094 -- 6
16 547 -- 7
8 274 -- 8
4 137 -- 9
2 69 -- 10
1 40 -- 11
1 20 -- 12
1 10 -- 13
1 5 -- 14
1 3 -- 15
1 2 -- 16
'''