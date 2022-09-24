from typing import List

def filtering(k, dic, string):
    if string in dic:
        string = "#" * len(string)
    if "." in string:
        for word in dic:
            for i in range(len(word)):
                for j in range(len(string)):
                    if i == j:
                        pass
                    elif i == ".":
                        string[j] = word[i]
                    else:
                        continue
    return string

def solution(k: int, dic: List[str], chat: str) -> str:
    answer = ''
    chat = chat.split(" ")
    for i in range(len(chat)):
        chat[i] = filtering(k, dic, chat[i])
    return " ".join(chat)