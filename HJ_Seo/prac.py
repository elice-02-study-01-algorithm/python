# 실험성 코드 페이지입니다. 백준이나 프로그래머스, 앨리스 문제 풀이 파일이 아녜요! - HJ -
#한글문서는 오픈 안됨.

import functools, itertools, random, math, time
import numpy as np #pandas, matplotlib 안깔림 

lst = [[0]] + [[] for _ in range(3)]
lst[1].append(5)

print(lst)


# a = []
# lst = [3,4,5,6,3,4]
# i=-1
# while True:
#     try:
#         i = lst.index(4,i+1)
#         a.append(lst.index(4,i))  #get err
#         print(i)
#     except:
#         break
# print(a)

# lst = [2,3]+[i for i in range(10)] + [2,3,4]
# print(lst)

# for i in range(2):
#     lst = [2,3]+[random.randint(1,1000000) for _ in range(1000000)]+[2,2,2]
    
#     start_time = time.time()
#     print(max(lst),min(lst))
#     a = []
#     j = 0
#     while True:
#         try:
#             a.append(lst.index(2,j))
#             j = lst.index(2,j+1)
#         except:
#             break
#     print(a)
#     print(time.time()-start_time)

# print([1,2,3,4])
# print(sum(itertools.compress([1,2,3,4,5,6], [2,0,1,0,1,1]))) # 뒤쪽에 뭘 넣어도 15가 return.

# a = {1,2,3,4}

# a.add(1)

# print(min(a))

# cnt = 0
# for i in itertools.cycle(range(6)):
#     print(i)
#     cnt+=1
#     if cnt == 20:
#         break


# def mul(a,b):
#     return a*b
# a = itertools.starmap(mul, [(1,2),(3,4)])
# print(next(a))
# print(next(a))

# print(sum(range(101)[0:10]))

# def lst_partition(iter,n,k):
#     if len(iter)%n == 0:
#         yield len(iter)//n
#     else:
#         yield len(iter)//n+1
#     a=0
#     while True:
#         b=0
#         lst=[]
#         for i in iter[a:a+n]:
#             lst.append(k%i)    #range로 가져갔기 때문에 코드변환이 안됨,, 
#         b += sum(lst)   #효율적이지 않음.
#         a += n
#         yield b


# def lst_partition(iter,n,k):
#     if len(iter)%n == 0:
#         yield len(iter)//n
#     else:
#         yield len(iter)//n+1
#     a=0
#     while True:
#         b=0
#         for i in iter[a:a+n]:   #요거 어떻게 수정이 안되나???..,,,, -- 이게 수정되야함. 수정이 잘 될시 아래 if문의 숫자를 많이 줄여도 좋음.
#             b += k%i
#         a += n
#         yield b

# print(divmod(176919,1701))
# print(divmod(17743986,176919))
# print(divmod(1775259165,17743986))
# print(divmod(177531881563,1775259165))
# print(divmod(17753288205204,177531881563))
# print(divmod(1775329577805763,17753288205204))
# print(divmod(177532965887639372,1775329577805763))
# print(860565**2)
# print(52086**2)
'''
100*2        --> 1701               , 476
1000*2       --> 176919             , 52169
10000*2      --> 17743986           , 5246486
100000*2     --> 1775259165         , 525284165
1000000*2    --> 177531881563       , 52532131563
10000000*2   --> 17753288205204     , 5253290705204
100000000*2  --> 1775329577805763   , 525329602805763
1000000000*2 --> 177532965887639372 , 52532966137639372


20000*2 --> 70995849 
2배면 4* + 잉여,
10배면 10* + 잉여..
'''

'''
10 20 --> 16
20 40 --> 68 .. 16*4 + 4
30 60 --> 151 ..16*9 + 7?
40 80 --> 306 .. 16*16 + 50..,,,? .. 68*4 + 34..,,?
'''