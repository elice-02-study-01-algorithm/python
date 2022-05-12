from sys import stdin

# p는 PPAP 문자열
# PPAP 문자열에서 p 하나를 PPAP로 바꾼 문자열은 PPAP 문자열
string = stdin.readline().strip()
stack = []
for i in string:
    if len(stack) >= 4:
        # PPAP를 다시 P로 치환하기 위해 PAP를 pop
        if stack[-4] == "P" and stack[-3] == "P" and stack[-2] == "A" and stack[-1] == "P":
            del stack[-3:]

    stack.append(i)

result = "".join(stack)
if result == "P" or result == "PPAP":
    print("PPAP")
else:
    print("NP")