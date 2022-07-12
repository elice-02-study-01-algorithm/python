#전위.. root first, left second, right third!... 
# return [root] + f[tree.left] + f[tree.right] 

#중위.. left first, right last, root Nob!... 
# return f[tree.left] + [root] + f[tree.right] 

#후위.. left first, right second, root last!... 
# return f[tree.left] + f[tree.right] + [root] 

#aim 전위, 중위를 받아서 후위를 뽑는 함수를 만들기.. 트리에 대한 복원이 없이 후위를 만들 수 있을까?

'''
input :
2
4
3 2 1 4
2 3 4 1
8
3 6 5 4 8 7 1 2
5 6 8 4 3 1 2 7
===========
output :
2 4 1 3
5 8 4 6 2 1 7 3
'''

case = int(input())

def both_to_post(lst1,lst2):
    root = 0
    # print(f'inputlst = {lst1}, {lst2}')
    left_part = []
    right_part = []

    if len(lst1)<=1:
        left_part = lst1
    elif len(lst2)<=1:
        right_part = lst2
    else:
        root = lst1[0]
        root_sight = lst2.index(root)

        left2 = lst2[:root_sight]
        right2 = lst2[root_sight+1:]

        left1 = lst1[1:len(left2)+1]
        right1 = lst1[-len(right2):]
        #==================================
        # print('l',left1,left2)
        # print('r',right1,right2)
        #==================================
        left_part = both_to_post(left1,left2)
        right_part = both_to_post(right1,right2)
    # print(left_part,right_part)
    if root == 0:
        return left_part + right_part
    return left_part + right_part + [root]

for i in range(case):
    v = int(input())
    lst1 = list(map(int,input().strip().split()))
    lst2 = list(map(int,input().strip().split()))

    print(' '.join(map(str,both_to_post(lst1,lst2))))


# lst1 = [1, 4]  #root = 1, left = 4.
# lst2 = [4, 1]
# print(both_to_post(lst1,lst2))  #aim : [4,1] done.
# print('==========')
# lst1 = [3, 2, 1, 4]
# lst2 = [2, 3, 4, 1]
# print(both_to_post(lst1,lst2))  #aim : [2,4,1,3] done.
# print('==============')
# lst1 = [3, 6, 5, 4, 8, 7, 1, 2]
# lst2 = [5, 6, 8, 4, 3, 1, 2, 7]
# print(both_to_post(lst1,lst2))  #aim : [5, 8, 4, 6, 2, 1, 7, 3] done.
# print('===================')
# print(both_to_post(lst1,lst2))

'''
1 
1
1 2 4 8 9 5 10 11 3 6 12 13 7 14 15... done
8 9 4 2 10 5 11 1 12 6 13 3 14 7 15
output : 9 8 4 10 11 5 2 12 13 6 14 15 7 3 1
'''

'''
1
1
1 2 3
2 1 3
output : 2 3 1
'''