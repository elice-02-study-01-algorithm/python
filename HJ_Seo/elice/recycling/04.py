from sys import stdin
from collections import deque
def main():
    N,K = map(int,stdin.readline().strip().split())

    people = dict()

    for i in range(1,N+1):
        people[i] = set(map(int,stdin.readline().strip().split()))

    current = deque([K])
    check = [False]*(N+1)
    discard = {K}

    while current:
        player = current.pop()
        if check[player] == False:
            current.extend(people[player])
            check[player] = True
            discard.update(people[player])

    print(N-len(discard))


if __name__=="__main__":
    main()