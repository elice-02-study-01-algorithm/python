import re
x = re.finditer('a','aaasdf11.asdfsadfasdf.qwerqwer.')
for i in x:
    print(i.span()[0])
n = int(input())
arr = input().strip()

if n<=25:
    print(arr)
else:
    arrlst = arr.split('.')
    # print(arrlst)
    leng = 0
    for i in arrlst:
        temp = len(i)+1
        
        leng += temp
        