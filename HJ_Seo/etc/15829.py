n = int(input())

arr = input()
r = 1

result = 0

for i in arr:
    result += (ord(i)-96)*r
    r *= 31
    if r > 1234567891:
        r %= 1234567891
    
print(result%1234567891)