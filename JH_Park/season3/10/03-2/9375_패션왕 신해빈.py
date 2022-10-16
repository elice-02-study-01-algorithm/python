import sys
input = sys.stdin.readline

case = int(input())
for _ in range(case):
    n = int(input())
    dress_dict = {}
    for _ in range(n):
        value, key = input().rstrip().split()
        if key in dress_dict:
            dress_dict[key] += 1
        else:
            dress_dict[key] = 1
    result = 1
    for key in dress_dict:
        result *= dress_dict[key] + 1
    print(result - 1)