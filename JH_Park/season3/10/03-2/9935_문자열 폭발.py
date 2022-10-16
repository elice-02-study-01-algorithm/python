import sys
input = sys.stdin.readline

# rstrip 이거 안 넣어주니까 '\n'가 배열 끝에 들어감
word = input().rstrip()
bomb = input().rstrip()

poped_list = []

bomb_len = len(bomb)

for w in word:
    poped_list.append(w)
    if bomb[-1] == w:
        if len(poped_list) >= bomb_len and ''.join(poped_list[-bomb_len:]) == bomb:
            del poped_list[-bomb_len:]

print("FRULA" if len(poped_list) == 0 else ''.join(poped_list))