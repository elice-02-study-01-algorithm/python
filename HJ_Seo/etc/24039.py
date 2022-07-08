Prime = [2]

for i in range(3,200):
    for j in Prime:
        if i%j == 0:
            break
    else:
        Prime.append(i)
        
Prime_square = []

for i in range(1,len(Prime)):
    Prime_square.append(Prime[i-1]*Prime[i])
    
N = int(input())

for i in Prime_square:
    if i>N:
        print(i)
        exit(0)        
