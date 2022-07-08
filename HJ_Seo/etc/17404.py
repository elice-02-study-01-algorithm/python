from sys import stdin

n = int(stdin.readline().strip())

house = [list(map(int,stdin.readline().strip().split())) for _ in range(n)]



# ! XXXXXXXX
'''
3
2 100 100
100 100 100
1 100 100
==> 201 (100, 100, 1)

3
26 40 83
49 60 57
13 89 99
==> 110(40, 57, 13)
'''