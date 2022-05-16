from sys import stdin

N = int(stdin.readline().strip())
lst = sorted(stdin.readline().strip().split())

M = int(stdin.readline().strip())
lst2 = stdin.readline().strip().split()

temp = lst2[0]
catch_one = {}
cnt = 0

for i in lst:
    if i in catch_one.keys():
        catch_one[i] += 1
    else:
        catch_one[i] = 1

print(' '.join(str(catch_one[m]) if m in catch_one else '0' for m in lst2))

#! dic에 대한 좋은 사실을 알게 되었다.