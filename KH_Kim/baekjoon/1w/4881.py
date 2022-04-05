# 백준
# 4881번 : 자리수의 제곱
import sys

##* 89, 1
##* 0< a,b < 10^9

# 1.숫자 제곱 합 함수
def square_fun(number):
    str_num = list(number)  # map -> list
    # print(str_num[0][0])  # 첫째 자리
    # print(str_num[0])    # 넘버
    # print(str_num)  # 리스트
    sum_next = 0
    # breakPoint = True
    while str_num.count(str_num[-1]) < 2:
        # if str_num.count(str_num[-1]) <2:
            # breakPoint = False
            # break
        for i in str_num[-1]:
            temp_num = int(i) * int(i)
            sum_next += temp_num
        str_num.append(str(sum_next))
    # print(str_num)   # 제곱합한 숫자 리스트에 추가, 루프 리스트 리턴
    return str_num


# 수열 길이
def count_list_fun(list_l):
    # temp = list_l.split(',')
    # length = len(temp)
    length = len(list_l)
    return length


# 재귀
def loop_fun(list_n):
    list_length = 0
    # loop_escape = False
    while True:

        added_next = square_fun(list_n)
        # for i in added_next:
        #     if i == added_next[-1]:
        #         list_length = count_list_fun(added_next)
        #         loop_escape = True
        #         break
        # if loop_escape == True:
        #     break
        if added_next[-1] in list_n:
            list_length = count_list_fun(added_next)
            break

    return list_length

def compare_fun(A, B):
    pass


##! 0 0 입력일경우 종료
if __name__ == '__main__':
    # while True:
    #     a, b = map(str, sys.stdin.readline().split())  # str
    #     if a == 0 and b == 0:
    #         break
    #     else:
    #         A_list = func(a)  # 제곱합 루프
    #         B_list = func(b)  # 
    #         print(a, b, output(A_list, B_list))
    a = map(str, sys.stdin.readline().split())  # str
    A_list = square_fun(a)
    print(A_list)

