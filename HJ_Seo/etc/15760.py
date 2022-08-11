'''
1 5 3 8 2, 1   
1 3 5 2 8, 2
1 3 2 5 8, 3
1 2 3 5 8, 4 .. return
'''

# n = int(input())
# lst = [int(input()) for _ in range(n)]

# leng = len(lst)-1
# last = sorted(lst.copy())
# result = 0

# while lst != last:
#     result += 1
#     print(lst)
#     for i in range(leng):
#         if lst[i+1] < lst[i]:
#             tmp = lst[i+1]
#             lst[i+1] = lst[i]
#             lst[i] = tmp

# print(lst)
# print(result)

# ! initial code.

# lst = []
# while True:
#     try:
#         lst.append(int(input()))
#     except:
#         break

# leng = len(lst)
# last = sorted(lst.copy())
# result = 0 # 항상 한번은 돈다... 아닌듯.. 그런데 틀렸네??

# lst_num = set(lst)
# num_idx_dict = dict()
# num_idx_dict_last = dict()

# for i in range(leng):
#     if lst[i] not in num_idx_dict:
#         num_idx_dict[lst[i]] = []
#     num_idx_dict[lst[i]].append(i)
    
#     if last[i] not in num_idx_dict_last:
#         num_idx_dict_last[last[i]] = []
#     num_idx_dict_last[last[i]].append(i)
    
# for i in lst_num:
#     num_idx_dict[i] = max(num_idx_dict[i])
#     num_idx_dict_last[i] = max(num_idx_dict_last[i])
#     result = max(result,num_idx_dict[i] - num_idx_dict_last[i])    

# # print(num_idx_dict)
# # print(num_idx_dict_last)

# print(result)

# ! second... fail.

n = int(input())
lst = [int(input()) for _ in range(n)]

leng = len(lst)
last = sorted(lst)
result = 0

num_idx_dict = dict()
num_idx_dict_last = dict()

for i in range(leng):
    num_idx_dict[lst[i]] = i
    num_idx_dict_last[last[i]] = i

for i in num_idx_dict:
    result = max(result,num_idx_dict[i] - num_idx_dict_last[i])    

# print(num_idx_dict)
# print(num_idx_dict_last)

print(result+1)

# ! third.. fail... fix. claer.. 첫 번째 수는 lst의 갯수더라... 아오 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
