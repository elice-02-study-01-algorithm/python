import sys

deque = []

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    command = list(map(str, sys.stdin.readline().rstrip().split(' ')))
    if command[0] == "push_back":
        deque.append(command[1])
    elif command[0] == "push_front":
        deque = [command[1]] + deque
    elif command[0] == "pop_front":
        if not deque:
            print(-1)
        else:
            print(deque[0])
            deque = deque[1:len(deque)]
    elif command[0] == "pop_back":
        if not deque:
            print(-1)
        else:
            print(deque.pop())
    elif command[0] == "size":
        print(len(deque))
    elif command[0] == "empty":
        if not deque:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if not deque:
            print(-1)            
        else:
            print(deque[0])
    elif command[0] == "back":
        if not deque:
            print(-1)          
        else:
            print(deque[-1])