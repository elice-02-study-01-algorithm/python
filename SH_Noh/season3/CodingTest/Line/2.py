from typing import List

def filtering(k, dic, string):
    if string in dic:
        string = "#" * len(string)
        return string
    # .이 대체할 수 있는 만큼 word에서 빼자
    if "." in string: # ex) bad.ord
        # .이 들어갈 수 있는 단어가 최대로 커버할 수 있는 길이
        max_len = len(string) + string.count(".") * (k - 1) # 8
        for word in dic:
            # 커버할 수 없는 길이면 return
            if len(word) > max_len:
                return string
            else:
                for i in range(len(word)):
                    for j in range(max_len):
                        if word[i] == string[j]:
                            continue
                        if string[j] == ".":
                            string[j] = word[i]
                        else:
                            continue

def solution(k: int, dic: List[str], chat: str) -> str:
    chat = chat.split(" ")
    for i in range(len(chat)):
        chat[i] = filtering(k, dic, chat[i])
    return " ".join(chat)

# print(solution(2, ["slang", "badword"], "badword ab.cd bad.ord .word sl.. bad.word"))
print(solution(2, ["slang", "badword"], "bad.ord"))
# print(solution(3, ["abcde", "cdefg", "efgij"], ".. ab. cdefgh .gi. .z."))
print(solution(3, ["abcde", "cdefg", "efgij"], "ab."))