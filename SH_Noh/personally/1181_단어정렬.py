from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    N = int(input())
    word = set()
    for _ in range(N):
        word.add(input())
    word = list(word)
    word.sort()
    word.sort(key = len)
    print(''.join(word))