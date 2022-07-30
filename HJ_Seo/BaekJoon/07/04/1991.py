from sys import stdin

n = int(input())

graph = dict()
for i in range(n):
    par,chi,chi2 = map(str,stdin.readline().strip().split())
    graph[par] = (chi,chi2)
    
def before(node):
    if node != '.':
        print(node,end = '')
        before(graph[node][0])
        before(graph[node][1])
    else:
        return

def mid(node):
    if node == '.':
        return
    else:
        mid(graph[node][0])
        print(node,end='')
        mid(graph[node][1])
        
    
def after(node):
    if node == '.':
        return
    else:
        after(graph[node][0])
        after(graph[node][1])
        print(node,end='')

node = 'A'

before(node)
print()
mid(node)
print()
after(node)

# 순회는 정의대로..