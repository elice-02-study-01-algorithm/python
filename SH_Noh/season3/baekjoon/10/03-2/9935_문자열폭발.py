from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    string = list(input().rstrip())
    bomb_str = list(input().rstrip())
    # 임시 스택에 넣어 비교하기
    tmp = []
    for i in range(len(string)):
        tmp.append(string[i])
        if tmp[-1] == bomb_str[-1] and len(tmp) >= len(bomb_str):
            if tmp[-len(bomb_str):] == bomb_str:
                # for i in range(len(bomb_str)):
                #     tmp.pop()
                del tmp[-len(bomb_str):]
    
    if tmp:
        print("".join(tmp))
    else:
        print("FRULA")
