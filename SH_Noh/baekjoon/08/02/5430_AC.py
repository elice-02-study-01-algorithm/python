from sys import stdin
input = stdin.readline

def func (functions, array):
    r, ld, rd = 0, 0, 0
    for func in functions:
        if func == "R":
            r += 1
        elif func == "D":
            if r % 2 == 0:
                ld += 1
            else:
                rd += 1

    if len(array) < ld + rd:
        return "error"
    else:
        if r % 2 == 1:
            array = array[::-1]
            result = array[rd:len(array)-ld]
            answer = ",".join(result)
        else:
            result = array[ld:len(array)-rd]
            answer = ",".join(result)
        return "[" + answer + "]"
        
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        functions = input().strip().replace("RR", "")
        n = int(input())
        array = input().strip()[1:-1].split(",")
        if n == 0:
            array = []
        print(func(functions, array))
