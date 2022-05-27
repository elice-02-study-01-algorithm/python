from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    while True:
        Input = input().split()
        if len(Input) == 1:
            break

        N, a, b = map(int, Input)
        x = 0
        playing = {x: 1}
        while True:
            # (a * x * x + b) % N
            # (((a % N) * (((x % N) * (x % N)) % N)) % N + (b % N)) % N
            x = (((a * x) % N) * (x % N) + b) % N
            if x in playing:
                playing[x] += 1
                if playing[x] == 3:
                    break
            else:
                playing[x] = 1
            
        justOnetime = list(playing.values()).count(1)
        # print(playing)
        print(N - len(playing) + justOnetime)