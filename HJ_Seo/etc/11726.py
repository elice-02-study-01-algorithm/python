n = int(input())
lst = [1,1,2]

if n <= 2:
    print(lst[n])
else:
    for i in range(n-2):
        lst.append(lst[-1]+lst[-2])

    print(lst[-1]%10007)
