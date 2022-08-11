n = input()

checknum = 1
while True:
    n_change = ''
    for i in n[:8]:
        n_change += chr(ord(i) ^ checknum)
    
    if n_change == 'CHICKENS':
        # print(checknum)
        break
    
    checknum += 1
    
n_before = 'CHICKENS'
for i in n[8:]:
    n_before += chr(ord(i) ^ checknum)

print(n_before)


# ! 이게 왜 정답이야???...
# for x in input():print(end=chr(ord(x)^22))