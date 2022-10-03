import re, sys
input = sys.stdin.readline

regex = re.compile('^[A-F]?A+F+C+[A-F]?$')

for _ in range(int(input())):
    print('Good' if regex.match(input()) == None else 'Infected!')