
def changer(word):
    if word[-1] == 'A':
        return word[:-1]+'B'
    elif word[-1] == 'B':
        return word[:-1]+'C'
    elif word[-1] == 'C':
        return word[:-1]+'D'
    elif word[-1] == 'D':
        return word[:-1]+'E'
    elif word[-1] == 'E':
        return changer(word[:-1])

def solution(word):
    
    check_word = changer(check_word)
    while check_word != word:
        check_word = ''
        answer = 0
        if len(check_word) < 5:
            check_word += 'Q'
            answer += 1
        else:
            answer += 1
            check_word = '11'
    return answer
