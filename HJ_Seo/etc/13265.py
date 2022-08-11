# https://www.acmicpc.net/problem/13265

from sys import stdin



case = int(stdin.readline().strip())

for _ in range(case):
    result = 'possible'
    v,e = map(int,stdin.readline().strip().split())
    
    red = set()
    blue = set()
    Vtx = set()
    tmp = []
    
    a,b = map(int,stdin.readline().strip().split())
    
    red.add(a)
    blue.add(b)
    Vtx.update([a,b])
    
    for _ in range(e-1):
        a,b = map(int,stdin.readline().strip().split())
        if a in Vtx or b in Vtx:
            if a in red:
                if b in blue:
                    continue
                elif b in red:
                    result = 'impossible'
                    break
                else:
                    blue.add(b)
                    Vtx.add(b)
            elif a in blue:
                if b in red:
                    continue
                elif b in blue:
                    result = 'impossible'
                    break
                else:
                    red.add(b)
                    Vtx.add(b)
            elif b in red:
                if a in blue:
                    continue
                elif a in red:
                    result = 'impossible'
                    break
                else:
                    blue.add(a)
                    Vtx.add(a)
            elif b in blue:
                if a in red:
                    continue
                elif a in blue:
                    result = 'impossible'
                    break
                else:
                    red.add(a)
                    Vtx.add(a)
        
        else:
            tmp.append((a,b),(b,a))
        
        if result == 'impossible':
            break
    
    # tmp에 남은거 처리하기..
    if result == 'possible':
        1
            
    print(result)