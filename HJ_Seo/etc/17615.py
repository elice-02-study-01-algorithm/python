from sys import stdin

n = stdin.readline()
rb = stdin.readline().rstrip()

print(min(rb.rstrip('R').count('R'),rb.rstrip('B').count('B'),rb.lstrip('R').count('R'),rb.lstrip('B').count('B')))