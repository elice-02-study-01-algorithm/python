n = input()

while True:
    sum = 0
    for i in n:
        sum += int(i)
    
    if int(n) % sum == 0:
        print(n)
        break

    n = str(int(n)+1)