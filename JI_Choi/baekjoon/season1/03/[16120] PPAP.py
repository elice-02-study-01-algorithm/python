import sys


def input():
    return sys.stdin.readline().rstrip()


word = input()

# 변환이 필요하지 않은 경우
if word == "P" or word == "PPAP":
    print("PPAP")

# 변환이 필요한 경우 (PPAP -> P)
else:
    stack = []
    ppap = ["P", "P", "A", "P"]
    for i in word:
        stack.append(i)
        if stack[-4:] == ppap:
            stack.pop()
            stack.pop()
            stack.pop()

    if stack == ppap or stack == ['P']:
        print("PPAP")
    else:
        print("NP")

# https://javaiyagi.tistory.com/600
