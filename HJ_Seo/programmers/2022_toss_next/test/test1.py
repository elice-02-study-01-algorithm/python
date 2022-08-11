def solution(s):
    s = s.lower() # ! 함정..ㄷㄷ
    cnt = 97
    wor = [97]
    for i in range(97,123):
        if s.count(chr(i)) == s.count(chr(cnt)):
            if i not in wor:
                wor.append(i)

        elif s.count(chr(i)) > s.count(chr(cnt)):
            cnt = i
            wor = [i]
    
    answer = ''
    # print(wor)
    for i in [116,111]:
        if i in wor:
            answer += chr(i).upper()
            wor.remove(i)

    if 115 in wor:
        answer += 'SS'
        wor.remove(115)

    for i in wor:
        answer += chr(i)

    return answer
