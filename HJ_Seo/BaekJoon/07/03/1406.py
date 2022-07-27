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
    
# print(arr) # ! arr를 무한 재생성하는 것이라 당연히 시간 초과.

class Node:
    def __init__(self, key=None):
        self.key = key
        self.prev = self
        self.next = self
    def __str__(self):
        return str(self.key)

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()

    def __iter__(self):
        v = self.head.next
        while v != self.head:
            yield v
            v = v.next
    def __str__(self): #키 값들을 join하여 print하는 스페셜메소드
        return "".join(str(v.key) for v in self)
    def splice(self, a, b, x):  #[a,b] 구간을 x 다음에 삽입하는 함수
        if a == None or b == None or x == None:
            return
        # 1. [a..b] 구간을 잘라내기 
        a.prev.next = b.next
        b.next.prev = a.prev

        # 2. [a..b]를 x 다음에 삽입하기
        x.next.prev = b
        b.next = x.next
        a.prev = x
        x.next = a
    def moveAfter(self, a, x):    #splice를 이용해서 a를 x 뒤로 이동하는 함수
        self.splice(a, a, x)

    def moveBefore(self, a, x):     #splice를 이용해서 a를 x 앞으로 이동하는 함수 
        self.splice(a, a, x.prev) 

    def insertBefore(self, x, key):    #moveBefore를 이용해서 x 앞에 Node(key)를 
        self.moveBefore(Node(key), x)    #삽입하는 함수
      
    def deleteNode(self, x): # delete x
        if x == None or x == self.head: 
            return
        # 노드 x를 리스트에서 분리해내기
        x.prev.next, x.next.prev = x.next, x.prev

from sys import stdin
L = DoublyLinkedList()
c = Node('|')
c.next = L.head
c.prev = L.head
L.head.next = c
L.head.prev = c

text = list(stdin.readline().strip())
for i in text:
        L.insertBefore(c, i)

N = int(stdin.readline().strip())  
for i in range(N):
    command = stdin.readline().strip()
    if command[0]== "L" and c.prev.key!=None :
        L.moveBefore(c, c.prev)
    elif command[0]=="D" and c.next.key!=None:
        L.moveAfter(c, c.next)
    elif command[0]=="B" and c.prev.key!=None:
        L.deleteNode(c.prev)
    else:
        L.insertBefore(c, command[2])


L.deleteNode(c)

print(L)