str = list(input())
ppap = []

while str:
    if "".join(str[:4]) == "PPAP":
        str.pop(0)
        str.pop(0)
        str.pop(0)
        str.pop(0)
        ppap.append("P")
    else:
        ppap.append(str[0])
        str.pop(0)

if "".join(ppap) == "PPAP":
    print("PPAP")
else:
    print("NP")
