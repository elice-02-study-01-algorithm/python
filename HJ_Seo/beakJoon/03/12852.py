# n = int(input())
# lst = [n]  

# while n != 1:
#     if n%81 == 1:
#         n -= 1
#         # print('c1',n)
#     elif n%3 == 0:
#         n = n//3
#         # print('c2',n)
#     elif n%2 == 0:
#         n = n//2
#         # print('c3',n)
#     else: 
#         n -= 1
#         # print('c4',n)
    
#     lst.append(n)

# print(len(lst) - 1)
# print(' '.join(map(str,lst)))

# print(2**16)  #wanted : 16 but cur_res = 18. 
# print(2**22)  #이거 24가 나옴.
# 21가 나와야하나 케이스에서는 28.
# 이거 어렵다..,,,
# 100 --> 100 50 25 24 8 4 2 1 : 7
# 10 --> 10 9 3 1 : 4
# 11 --> 11 10 9 3 1 : 5
# 12 --> 12 4 2 1 : 4
# 13 --> 13 12 4 2 1 : 5
# 14 --> 14 7 6 2 1 : 5
# 15 --> 15 5 4 2 1 : 5
# ....
#해야 할 것!
#arr_lst를 최소길이 list로 채우게 만들기. 그후 점화식에 따라 return.

n = int(input())
arr_lst = [[0],[1],[1,2],[1,3]] #0번째는 무시, 차례대로 1~3의 최소 lst.
len_arr_lst = [1,1,2,2]

def make_lst(n):
    if n <= 3:
        return len_arr_lst[n],arr_lst[n]
    
    a2,a3,a_1 = 0,0,0
    for i in range(4,n+1):
        if i%2 == 0 and i%3 == 0:
            a2 = len_arr_lst[i//2]
            a3 = len_arr_lst[i//3]
            a_1 = len_arr_lst[i-1]
            A2 = arr_lst[i//2]
            A3 = arr_lst[i//3]
            A_1 = arr_lst[i-1]

            if min(a2,a3,a_1) == a2:
                len_arr_lst.append(a2+1)
                arr_lst.append(A2+[i])
            elif min(a2,a3,a_1) == a3:
                len_arr_lst.append(a3+1)
                arr_lst.append(A3+[i])
            else:
                len_arr_lst.append(a_1+1)
                arr_lst.append(A_1+[i])

        elif i%3 == 0:
            a3 = len_arr_lst[i//3]
            a_1 = len_arr_lst[i-1]
            A3 = arr_lst[i//3]
            A_1 = arr_lst[i-1]

            if min(a3,a_1) == a3:
                len_arr_lst.append(a3+1)
                arr_lst.append(A3+[i])
            else:
                len_arr_lst.append(a_1+1)
                arr_lst.append(A_1+[i])

        elif i%2 == 0:
            a2 = len_arr_lst[i//2]
            a_1 = len_arr_lst[i-1]
            A2 = arr_lst[i//2]
            A_1 = arr_lst[i-1]

            if min(a2,a_1) == a2:
                len_arr_lst.append(a2+1)
                arr_lst.append(A2+[i])
            else:
                len_arr_lst.append(a_1+1)
                arr_lst.append(A_1+[i])

        else:
            a_1 = len_arr_lst[i-1]
            A_1 = arr_lst[i-1]
            len_arr_lst.append(a_1+1)
            arr_lst.append(A_1+[i])

    return len_arr_lst[n],arr_lst[n]

leng, lst = make_lst(n)
lst.reverse()
print(leng-1)
print(' '.join(map(str,lst)))

#done. 더 효율적인 코드를 짤 수 있지 않을까?? Think!!!