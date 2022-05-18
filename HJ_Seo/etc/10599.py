while True:
    k = input().strip()
    if k == '0 0 0 0':
        break 
    
    a,b,c,d = map(int,k.split())
    
    print(c-b,d-a)