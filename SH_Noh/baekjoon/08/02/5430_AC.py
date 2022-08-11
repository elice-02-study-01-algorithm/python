from collections import deque
from sys import stdin
input = stdin.readline

def func (functions, array):
    for func in functions:
        if func == "R":
            array = deque(reversed(array))
        elif func == "D":
            if len(array) == 0:
                return "error"
            array.popleft()
    return array

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        functions = input().strip().replace("RR", "")
        n = int(input())
        array = deque(input().strip()[1:-1].split(","))
        if n == 0:
            array = deque([])
        result = func(functions, array)
        if result != "error":
            result = "[" + ",".join(result) + "]"
        print(result)