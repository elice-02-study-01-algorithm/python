#이진트리의 너비

# class Tree:
#     def __init__(self,i,l,r):
#         self.index = i
#         self.left = l
#         self.right = r
    
#     def addNode(self,i,l,r):
#         if l == -1:
#             l = None
#         if r == -1:
#             r = None
        
#         if self.index == None or self.index == i:
#             self.index = i
#             self.left = Tree(l,None,None)
#             self.right = Tree(r,None,None)

# nbr = int(input())

# t = Tree(None,None,None)

# for _ in range(nbr):
#     i,l,r = map(int,input().strip().split())
#     t.addNode(i,l,r)

# #print(len(t)) length가 없다..?..

def Fact(n):
    if type(n) != int:
        print('정수를 입력해주세요.')
        return 
    while n>0:
        return n*Fact(n-1)
    else:
        return 1

print(Fact(5))