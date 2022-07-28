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
    if a[i] == b[i] and a[i] == '1':
        op_and += '1'
    else:
        op_and += '0'
        
    if a[i] == '1' or b[i] == '1':
        op_or += '1'
    else:
        op_or += '0'
    
    if maxi>i:
        op_xor += '0'
    elif a[i] != b[i]:
        op_xor += '1'
    else:
        op_xor += '0'
    
    if a[i] == '1':
        not_a += '0'
    else:
        not_a += '1'
        
    if b[i] == '1':
        not_b += '0'
    else:
        not_b += '1'
        
print(op_and)
print(op_or)
print(op_xor)
print(not_a)
print(not_b)