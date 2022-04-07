
lst1 = [1, 4]  #root = 1, left = 4.
lst2 = [4, 1]

root = lst1[0]
root_sight = lst2.index(root)  #index를 통한 root의 위치.. 현재 0

left2 = lst2[:root_sight]
right2 = lst2[root_sight+1:]

left1 = lst1[1:len(left2)+1]
right1 = lst1[-len(right2)+2:]

print(left1,left2)
print(right1,right2)