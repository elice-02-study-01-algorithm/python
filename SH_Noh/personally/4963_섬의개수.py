from sys import stdin
input = stdin.readline

def countIsland(Map):
    pass

if __name__ == "__main__":
    while True:
        width, height = map(int, input().split())
        if (width, height) == (0, 0):
            break
        Map = [list(map(int, input().split())) for _ in range(height)]
        print(Map)
        countIsland(Map)