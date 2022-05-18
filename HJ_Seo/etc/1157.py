arr = input()
arr = arr.upper()

alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = []

for i in alp:
    num.append(arr.count(i))

if num.count(max(num)) > 1:
    print('?')
else:
    print(alp[num.index(max(num))])
