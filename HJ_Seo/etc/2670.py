#연속 부분 최대곱.
import math 

def mul_list(lst):
    if len(lst) == 1:
        return lst[0]

    mul = lst[0]
    for i in lst[1:]:
        mul = round(mul*i,3)
    return mul

n = int(input())
lst = []
for i in range(n):
    lst.append(float(input()))

while lst[0] == 0.0:
    lst = lst[1:]

while lst[-1] == 0.0: #앞뒤 0.0 싸그리 제거.
    lst.pop()
# print(lst)
temp = 1.0
new_lst = []
for i in range(len(lst)):
    if temp == 1.0:
        temp = lst[i] 
    elif lst[i] == 0:
        new_lst.append(temp)
        temp = 1
    elif temp>1 and lst[i]>1:
        temp = round(temp*lst[i],3)
    elif temp<1 and lst[i]<1:
        temp = round(temp*lst[i],3)
    else:
        new_lst.append(temp)
        temp = lst[i]

    if i == len(lst)-1 and temp != 1.0:
        new_lst.append(temp)

result = -math.inf

for i in range(len(new_lst)):
    for j in range(i+1,len(new_lst)):
        result = max(result, mul_list(new_lst[i:j]))
        # print(i,j,'==>',new_lst[i:j])

dot_index = str(result).index('.')
diff = len(str(result))-dot_index

if diff < 4:
    a = '0'*(4-diff)
    print(str(result)+a)
else:
    print(result)

# print(new_lst)
# print(round(1.55555,3)) # 소수 셋째자리에서반올림.


# result = 1.412
# dot_index = str(result).index('.')

# print(len(str(result))-dot_index)  #4