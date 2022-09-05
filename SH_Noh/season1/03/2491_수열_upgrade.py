from sys import stdin
input = stdin.readline

def calcLength(seq):
    count = 1
    maxCount = 1
    for i in range(N-1):
        if seq[i] <= seq[i+1]:
            count += 1
        else:
            if count > maxCount:
                maxCount = count
            count = 1
    if count > maxCount:
        maxCount = count
    return maxCount

if __name__ == "__main__":
    N = int(input())
    sequence = list(map(int, input().split()))
    print(max(calcLength(sequence), calcLength(sequence[::-1])))