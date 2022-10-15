# 사전에 A E I O U 만 사용하여 길이 5 이하의 모든 단어가 수록되어 있음
# 사전 특성상 알파벳 순으로 정렬되어 있음

# 백트래킹
def backtracking(word, tmp_word):
    global num, answer
    # print(tmp_word, num)
    if tmp_word == word:
        return num
    if len(tmp_word) == 5:
        return

    for w in word_list:
        num += 1
        tmp_word.append(w)
        answer = backtracking(word, tmp_word)
        if answer:
            return answer
        tmp_word.pop()
    
word_list = ["A", "E", "I", "O", "U"]
num = 0
answer = ''

def solution(word):
    tmp_word = []
    backtracking(list(word), tmp_word)
    
    return answer