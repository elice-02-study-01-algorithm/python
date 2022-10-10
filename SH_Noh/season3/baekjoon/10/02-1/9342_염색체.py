from sys import stdin
input = stdin.readline
import re

# A/B/C/D/E/F -> F -> C -> A/B/C/D/E/F
def validate(string):
    rule = re.compile("^[A-F]?A+F+C+[A-F]?$")
    result = rule.match(string)
    return result

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        string = input()
        print("Good" if validate(string) == None else "Infected!")