# n = (k * (k+1)) // 2.
# a,b ==> <a[0]+b[0],a[1]+b[1]>


def cord(n):
    a,b = 1,1

    while True:
        if ( a * (a+1) ) //2 >= n:
            break
        
        a+=1
    
    diff = ( a * (a+1) ) //2 - n
    
    while diff != 0:
        a -= 1
        b += 1
        diff -= 1
    
    return a,b

def change(a,b):
    k = a+b-1
    n = (k*(k+1))//2    
    
    return n-b+1

n = int(input())

for i in range(n):
    a,b = map(int,input().strip().split())
    v1,v2 = cord(a),cord(b)
    print(change(v1[0]+v2[0],v1[1]+v2[1]))