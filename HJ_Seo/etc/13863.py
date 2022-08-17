# https://www.acmicpc.net/problem/13863

# num = int(input())
# last = int(num**(1/3))+1
# three_sqr = [i**3 for i in range(1,last)] # 44777444 < 356**3 --> len(three_sqr) <= 356
# origin = [i for i in range(1,last)]
# def sum_max(num,lst):
#     lst2 = []
#     for i in lst[::-1]:
#         tmp = num//i
#         lst2.append(tmp)
#         num -= i*tmp
    
#     return lst2[::-1],sum(lst2)

# def check_comb(num,lst,origin):    
#     leng = len(lst)
#     result1 = 44777444
#     result2 = []
#     for i in range(leng,0,-1):
#         mult,cnt = sum_max(num,lst[:i]) # --> 재귀로 들어가야 할 것 같은데..?..
#         # print(mult,cnt)
#         if cnt<result1:
#             result1 = cnt
#             result2 = mult
    
#     last_result = []
#     for i in range(len(result2),0,-1):
#         numb = origin[i-1]
#         leng2 = result2[i-1]
#         if leng2 != 0:
#             last_result.extend([numb for _ in range(leng2)])
            
    
#     print(result1)
#     print(*last_result)
#     return

# check_comb(num,three_sqr,origin)

# ! 틀림..!.. 역시 짐작대로 재귀가 들어가야 할듯.


num = int(input())
last = int(num**(1/3))+1
three_sqr = (i**3 for i in range(1,last)) # 44777444 < 356**3 --> len(three_sqr) <= 356
origin = [i for i in range(1,last)]

def sum_max(num,lst,lst2=[]):
    if len(lst) == 0 or num == 0:
        return lst2,sum(lst2)
    
    first = lst[-1]
    tmp0 = num//first
    # for i in range(tmp0):
    #     num -= first
    #     comp1,comp2 = sum_max(num,lst,lst2)
    #     if ~~~
    
    lst2.append(tmp0)
    
    num -= first*tmp0
    
    comp1,comp2 = sum_max(num,lst[:-2],lst2)
    
    for i in lst[1:][::-1]:
        tmp = num//i
        lst2.append(tmp)
        num -= i*tmp
    
    if comp2 < sum(lst2):
        return comp1,comp2+tmp0
    
    return lst2,sum(lst2)+tmp0

### 42를 넣었을 때 mult,cnt에는 [2,5],7 가 들어가있어야 함. 

def check_comb(num,lst,origin):    
    leng = len(lst)
    result1 = 44777444
    result2 = []
    for i in range(leng,0,-1):
        mult,cnt = sum_max(num,lst[:i]) # --> 재귀가 들어가야 할 것 같은데..?..
        print(mult,cnt)
    #     if cnt<result1:
    #         result1 = cnt
    #         result2 = mult[::-1]
    
    # last_result = []    # 결과 완성 코드.
    # # print('result = ',result1,result2)
    # for i in range(len(result2),0,-1):
    #     numb = origin[i-1]
    #     leng2 = result2[i-1]
    #     if leng2 != 0:
    #         last_result.extend([numb for _ in range(leng2)])
            
    
    # print(result1)
    # print(*last_result)
    return

check_comb(num,three_sqr,origin)
