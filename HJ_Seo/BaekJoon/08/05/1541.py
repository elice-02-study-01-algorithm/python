from sys import stdin

f = stdin.readline().strip().split('-')

for i in range(len(f)):
    f[i] = f[i].split('+')
    num = 0
    for j in f[i]:
        num += int(j)
    
    f[i] = num

print(f[0]-sum(f[1:]))
 