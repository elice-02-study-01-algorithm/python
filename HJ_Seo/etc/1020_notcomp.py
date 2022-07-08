def num_sum(arr):
    dic = {i:0 for i in range(2,8)}
    for x in arr:
        if x == '1':
            dic[2] += 2
        elif x == '7':
            dic[3] += 3
        elif x == '4':
            dic[4] += 4
        elif x in ['2','3','5','9']:
            dic[5] += 5
        elif x in ['0','6']:
            dic[6] += 6
        elif x == '8':
            dic[7] += 7
    
    return sum(dic.values())
        
def next_num(arr,leng):
    x = str(int(arr)+1)
    if len(x)>leng:
        return '0'*leng
    else:
        return '0'*(leng-len(x))+x

num = input()
leng = len(num)
cnt = 1
num_sum_init = num_sum(num)

while True:
    num = next_num(num,leng)
    # print(num)
    if num_sum(num) == num_sum_init:
        print(cnt)
        break

    cnt += 1

# ! 3rd.. 더느림..

# num = input()
# leng = len(num)

# if num.count('1') == leng or num.count('8') == leng:
#     print('1'+'0'*leng)
#     exit(0)
    
# cnt1 = 0
# if num.endswith('1') or num.endswith('8'):
#     temp = num[-1]
#     for i in range(len(num)):
#         if num[-i] == temp:
#             cnt1 += 1
#         else:
#             break

# num = num[:-cnt1]
# leng = len(num)

# cnt_dict = {'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':5,'0':6}
# num_sum = 0
# for i in num:
#     num_sum += cnt_dict[i]

# print(num,num_sum)
# cnt = 1
# num = int(num)

# while True:
#     result = 0
#     num += 1
#     str_num = str(num)
    
#     if len(str_num) > leng:
#         str_num = '0'
#         num = 0
    
#     for i in str_num:
#         result += cnt_dict[i]
    
#     result += (leng - len(str_num)) * 6
    
#     if num_sum == result:
#         print(cnt* (10**cnt1))
#         break
#     cnt += 1
    

# 어떤 이유일까??   
# ex 1111111111 (1 10개.)
# ex2 71111111


# # ! inital code.
# num = input()
# leng = len(num)
    
# cnt_dict = {'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':5} # '0':6 
# num_sum = 0
# for i in num:
#     num_sum += cnt_dict[i]
    

# cnt = 1
# num = int(num)

# while True:
#     result = 0
#     num += 1
#     str_num = str(num)
    
#     if len(str_num) > leng:
#         str_num = '0'
#         num = 0
    
#     for i in str_num:
#         result += cnt_dict[i]
    
#     result += (leng - len(str_num)) * 6
    
#     if num_sum == result:
#         print(cnt)
#         print('0'*(leng-len(str(num)))+str(num))
#         break
#     cnt += 1
    
    
    
