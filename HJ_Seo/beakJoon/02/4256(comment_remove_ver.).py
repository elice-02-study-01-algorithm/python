#4256 트리
case = int(input())

def both_to_post(lst1,lst2):
    root = 0
    
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
        
        left_part = both_to_post(left1,left2)
        right_part = both_to_post(right1,right2)
    if root == 0:
        return left_part + right_part
    return left_part + right_part + [root]

for i in range(case):
    v = int(input())
    lst1 = list(map(int,input().strip().split()))
    lst2 = list(map(int,input().strip().split()))

    print(' '.join(map(str,both_to_post(lst1,lst2))))

