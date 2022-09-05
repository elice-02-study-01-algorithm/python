# https://www.acmicpc.net/problem/18054

from sys import stdin

cases = int(stdin.readline().strip())

vir_arr = []
anti_vir_arr = []
for i in range(cases):
    dna = stdin.readline().strip()
    leng = len(dna)
    for i in range(1,leng//2+1):
        if leng%i == 0 and dna[:i]*(leng//i) == dna:
            vir_arr.append(i)
            break
    else:
        vir_arr.append(leng)

for i in range(cases):
    dna = stdin.readline().strip()
    leng = len(dna)
    for i in range(1,leng//2+1):
        if leng%i == 0 and dna[:i]*(leng//i) == dna:
            anti_vir_arr.append(i)
            break
    else:
        anti_vir_arr.append(leng)
            
vir_arr = sorted(vir_arr)
anti_vir_arr = sorted(anti_vir_arr)

result = 0
for i in range(len(vir_arr)):
    result += (vir_arr[i]-anti_vir_arr[i])**2

print(result)
