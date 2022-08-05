from sys import stdin

n,m = map(int,stdin.readline().strip().split())

def song_to_bit(arr,m):
    num = 0
    for i in range(m):
        if arr[i] == 'Y':
            num += (1<<i)
    
    return num

def bit_cnt(num,m):
    cnt = 0
    for i in range(m):
        if num & (1<<i):
            cnt += 1
    
    return cnt

lst = []

check_num = 0
for i in range(n):
    git, arr = map(str,stdin.readline().strip().split())
    done = song_to_bit(arr,m)
    lst.append([done,[git]])
    check_num += done
    
if check_num == 0:
    print(-1)
    exit(0)

first = lst.copy()
next_comb = []
last_comb = lst.copy()

while True:
    
    for i in first:
        for j in lst:
            if i[0] | j[0] != max(i[0], j[0]):
                tmp = [i[0] | j[0], sorted(i[1]+j[1])]
                if tmp not in next_comb + last_comb:
                    next_comb.append(tmp)

    if len(next_comb) == 0:
        break
    
    last_comb.extend(next_comb)
    first = next_comb
    next_comb = []

xxx = sorted(last_comb,key = lambda x: (-bit_cnt(x[0],m),len(x[1])))
print(len(xxx[0][1]))
