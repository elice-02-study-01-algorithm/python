# 평행사변형.

# 평생사변병이 만들어지는 경우 D가 나올 수 있는 경우는 총 3가지.. 
# 어떤 평행사변형이든 항상 다른 평행사변형과 두 변을 공유하므로 그냥 2*maxleng-2*minleng을 해주면 된다.
# caution!! : 삼각형이 만들어지지 않는 케이스에 대해 잘 생각해보자.
# 1. 최소 두 점이 같은 경우.. 
# ==> 이때는 minleng==0이 된다.
# 2. 세 점이 서로 다르지만 일직선 상에 있을때.. 가장 긴 변의 길이가 나머지 두 변의 길이의 합과 같게 된다.
# ==> 2*maxleng == leng1+leng2+leng3가 된다.
# 51%?에서 틀렸는데 왜 틀린걸까??.... 아마도 계산상의 문제인 것 같다는 생각이 든다. 기울기로 변경후 end.

import math

x1,x2,y1,y2,z1,z2 = map(int,input().strip().split())


leng1 = math.sqrt((x1-y1)**2+(x2-y2)**2)
leng2 = math.sqrt((x1-z1)**2+(x2-z2)**2)
leng3 = math.sqrt((y1-z1)**2+(y2-z2)**2)

maxleng = max(leng1,leng2,leng3)
minleng = min(leng1,leng2,leng3)

if ((x1-y1)*(x2-z2)==(x1-z1)*(x2-y2)):
    print(-1.0)
else:
    print(2*(maxleng-minleng))