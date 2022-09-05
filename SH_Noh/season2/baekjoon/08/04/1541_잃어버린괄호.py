from sys import stdin
input = stdin.readline

# - 이후의 +는 다 -로 치환
# - 이후의 -도 -로 계산
# if __name__ == "__main__":
    # formula = input().strip().split("-")
    # init = map(int, formula.pop(0).split("+"))
    # result = sum(init)
    # for i in formula:
    #     seperate = list(map(int, i.split("+")))
    #     result -= sum(seperate)
    # print(result)

if __name__ == "__main__":
    formula = input().strip().split('-')
    result = 0
    for i in formula[0].split('+'):
        result += int(i)
    for i in formula[1:]:
        for j in i.split('+'):
            result -= int(j)
    print(result)