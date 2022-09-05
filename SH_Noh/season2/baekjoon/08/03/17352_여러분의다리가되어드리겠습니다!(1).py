# 두 개로 나눠진 영역의 양 끝단 중 아무거나 이어주면 됨
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution(graph, visited, island):
    # print(island)
    visited[island] += 1
    for i in graph[island]:
        if visited[i] == 0:
            solution(graph, visited, i)
        else:
            visited[i] += 1

if __name__ == "__main__":
    N = int(input())
    graph = {x: [] for x in range(1, N + 1)}
    for _ in range(N-2):
        i1, i2 = map(int, input().split())
        graph[i1].append(i2)
        graph[i2].append(i1)
    visited1 = [0] * (N + 1)
    visited2 = [0] * (N + 1)

    solution(graph, visited1, 1)
    a = visited1.index(1)
    next = visited1.index(0, 1)
    solution(graph, visited2, next)
    b = visited2.index(1)
    # print(graph)
    # print(visited)
    print(a, b)