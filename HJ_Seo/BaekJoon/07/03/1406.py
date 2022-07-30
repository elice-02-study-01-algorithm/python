# from sys import stdin

# arr = stdin.readline().strip()

# l = len(arr)
# n = int(input())

# while n != 0:
#     x = stdin.readline().strip()
    
#     if x[0] == 'L':
#         l = max(0,l-1)
#     elif x[0] == 'D':
#         l = min(len(arr),l+1)
#     elif x[0] == 'B':
#         if l != 0:
#             arr = arr[:l-1] + arr[l:]
#             l -= 1
#     else:
#         arr = arr[:l] + x[2:] + arr[l:]
#         l += 1
        
#     n -= 1
    
# print(arr) # ! first. arr를 무한 재생성하는 것이라 당연히 시간 초과.

# from sys import stdin

# class Node:
#     def __init__(self, key=None):
#         self.key = key
#         self.prev = self
#         self.next = self
        
#     def __str__(self):
#         return str(self.key)

# class Double_link:
#     def __init__(self):
#         self.head = Node()
        
#     def __iter__(self):
#         v = self.head.next
#         while v != self.head:
#             yield v
#             v = v.next
    
#     def __str__(self):
#         return ''.join(str(v.key) for v in self)
    
#     def splice(self, a, b, x):
#         if a == None or b == None or x == None:
#             return
        
#         a.prev.next = b.next
#         b.next.prev = a.prev 
#         # ~~~ (a ~ b) ~~~  : (a ~ b) 날리기 ## a == b : (a) 날리기.
        
#         b.next = x.next
#         x.next.prev = b
#         a.prev = x
#         x.next = a
#         # ~~~ x (a ~ b)  ~~~ .  
#         # ## a == b : 앞 두 줄에서 (x & a), x.next(x.next.prev == a) 뒤 두 줄에서 x, a, x.next  
    
#     def before(self, a, x):
#         self.splice(a, a, x.prev)
    
#     def after(self, a, x):
#         self.splice(a, a, x)
        
#     def insert_one(self, a, x):
#         self.before(Node(a), x)
        
#     def del_node(self,x):
#         if x == None or x == self.head: 
#             return
        
#         x.prev.next, x.next.prev = x.next, x.prev

# L = Double_link()
# c = Node('|')
# c.next = L.head
# c.prev = L.head
# L.head.next = c
# L.head.prev = c

# text = list(stdin.readline().strip())
# for i in text:
#     L.insert_one(i,c)
    
# N = int(stdin.readline().strip())
# for _ in range(N):
#     arr = stdin.readline().strip()
#     if arr == 'L' and c.prev.key != None:
#         L.before(c,c.prev)
#     elif arr == 'D' and c.next.key != None:
#         L.after(c,c.next)
#     elif arr =='B' and c.prev.key != None:
#         L.del_node(c.prev)
#     elif arr.startswith('P'):  # ! 여기서 왜 else가 들어가면 안되는걸까??..
#         L.insert_one(arr[2],c)

# L.del_node(c)

# print(L)
    
# ! second.. done but long time.


from sys import stdin
from collections import deque

left = deque()
right = deque()

arr = stdin.readline().strip()
for i in arr:
    left.append(i)

N = int(input())

for _ in range(N):
    arr = stdin.readline().strip()
    if arr == 'L' and left:
        right.append(left.pop())
    elif arr == 'D' and right:
        left.append(right.pop())
    elif arr =='B' and left:
        del left[-1] #left.pop()
    elif arr.startswith('P'):  # ! 여기서 왜 else가 들어가면 안되는걸까??..
        left.append(arr[2])

while right:
    left.append(right.pop())
    
if len(left) > 1:
    print(''.join(left))
elif len(left) == 1:
    print(left[0])
else:
    print()

# good.