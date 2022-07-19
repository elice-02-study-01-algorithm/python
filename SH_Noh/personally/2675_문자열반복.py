from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        R, S = input().split()
        R = int(R)
        string = []
        for i in S:
            print(i * R, end = '')
        print()
        #     string.append(i * R)
        # print(''.join(string))
