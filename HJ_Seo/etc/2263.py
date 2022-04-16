# from sys import stdin

# def both_to_pre(s1,s2):  #s1: inorder, s2: postorder.
#     if len(s1) <= 1:
#         return s1
#     elif len(s2) <= 1:
#         return s2

#     root = s2[-1]
#     root_index = s1.index(root)

#     left1 = s1[:root_index]
#     left2 = s2[:root_index]
#     right1 = s1[root_index+1:]
#     right2 = s2[root_index:-1]
    
#     left = both_to_pre(left1,left2)
#     right = both_to_pre(right1,right2)

#     return (root,) + left + right

# n = input()
# s1 = tuple(map(str,stdin.readline().strip().split()))
# s2 = tuple(map(str,stdin.readline().strip().split()))

# if __name__ == '__main__':
#     if len(s1) == 1:
#         print(s1)
#     else:
#         root = s2[-1]
#         root_index = s1.index(root)

#         left1 = s1[:root_index]
#         left2 = s2[:root_index]
#         right1 = s1[root_index+1:]
#         right2 = s2[root_index:-1]
        
#         left = both_to_pre(left1,left2)
#         right = both_to_pre(right1,right2)
        
#         pre_lst = (root,) + left + right

#         print(' '.join(pre_lst))

#메모리 초과..?... -->  list를 튜플로 바꿈.
# --> 메모리 초과2   --> sys.stdin 이용 + __main만 사용.
# --> 메모리 초과3  --> 검색을 통해 알게 된 사실.. 배열을 일일히 자르는 것은 매모리를 과도하게 소모.. 인덱스를 이용해서 만들자.
#
# AIM : s1,s2는 고정, 오로지 int index만을 이용해서 both_to_pre를 완성시키자..!

  
from sys import stdin

def both_to_pre(s1,s2,s1_start,s1_end,s1_root_location,s2_start,s2_end,s2_root_location):  #s1: inorder, s2: postorder.
    if len(s1) <= 1:
        return s1
    elif len(s2) <= 1:
        return s2

    root = s2[-1]
    root_index = s1.index(root)

    left1 = s1[:root_index]
    left2 = s2[:root_index]
    right1 = s1[root_index+1:]
    right2 = s2[root_index:-1]
    
    left = both_to_pre(left1,left2)
    right = both_to_pre(right1,right2)

    return (root,) + left + right

n = input()
s1 = tuple(map(str,stdin.readline().strip().split()))
s2 = tuple(map(str,stdin.readline().strip().split()))

root = s2[-1]
s1_root_location = s1.index[root]
s2_root_location = s2.index[root]
s1_end = len(s2)


pre_lst = both_to_pre(s1,s2,s1_start,s1_end,s1_root_location,s2_start,s2_end,s2_root_location)

print(' '.join(pre_lst))

'''
15
8 9 4 2 10 5 11 /1 /12 6 13 3 14 7 15
9 8 4 10 11 5 2 /12 13 6 14 15 7 3 /1
output : 1 2 4 8 9 5 10 11 3 6 12 13 7 14 15
'''