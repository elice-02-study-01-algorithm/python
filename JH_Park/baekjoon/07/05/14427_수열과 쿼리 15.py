import sys
import heapq


def main():
    N = int(sys.stdin.readline())
    A = [int(x) for x in sys.stdin.readline().split()]
    heap = [(a_i, i + 1) for i, a_i in enumerate(A)]
    heapq.heapify(heap)
    M = int(sys.stdin.readline())
    for i in range(M):
        query = [int(x) for x in sys.stdin.readline().split()]
        if query[0] == 1:
            _, i, v = query
            heapq.heappush(heap, (v, i))
            A[i - 1] = v
            while heap[0][0] != A[heap[0][1] - 1]:
                heapq.heappop(heap)
        else:
            print(heap[0][1])


if __name__ == '__main__':
    main()