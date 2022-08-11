def solution(X, Y):
    answer = "-1"
    # 첫 번째 문자열에서 두 번째 문자열이 겹치는 것 비교
    duplicate = []
    Y = list(Y)
    for i in X:
        if i in Y:
            # Y = Y.replace(i, "", 1)
            Y.remove(i)
            duplicate.append(i)
    if len(duplicate) != 0:
        answer = "".join(sorted(duplicate, reverse = True))
        if int(answer) == 0:
            answer = "0"

    return answer

# 73.7점


from collections import Counter
def solution(X, Y):
    answer = ""
    countX = Counter(X)
    countY = Counter(Y)
    keyX = sorted(countX.keys(), reverse = True)
    keyY = countY.keys()

    for i in keyX:
        if i in keyY:
            num = min(countX[i], countY[i])
            answer += i * num

    if answer == '':
        answer = "-1"
    elif int(answer) == 0:
        answer = "0"

    return answer

# 73.7점
# 얘가 좀 더 빠름