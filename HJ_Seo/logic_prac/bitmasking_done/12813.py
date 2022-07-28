from sys import stdin
a = stdin.readline().strip()
b = stdin.readline().strip()

op_and = ''
op_or = ''
op_xor = ''
maxi = min(a.index('1'),b.index('1'))
not_a = ''
not_b = ''
for i in range(100000):
    op_and += '1' if a[i] == b[i] and a[i] == '1' else '0'
    op_or += '1' if a[i] == '1' or b[i] == '1' else '0'
    not_a += '0' if a[i] == '1' else '1'
    not_b += '0' if b[i] == '1' else '1'
    
    if maxi>i:
        op_xor += '0'
    elif a[i] != b[i]:
        op_xor += '1'
    else:
        op_xor += '0'
    
print(op_and)
print(op_or)
print(op_xor)
print(not_a)
print(not_b)