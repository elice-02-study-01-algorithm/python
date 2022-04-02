# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 12:23:02 2022

@author: 형준
"""

 # s4 4881 자리수의 제곱.
'''
문제를 나눌 필요성이 보임.
1. 각 자릿수의 제곱을 리스트에 넣기.
2. 각 리스트에서 만나는 숫자의 최소를 넣기..(ex 참조.)
3. 이때 각 숫자의 처음을 만나거나 중간에 만나는 경우?...
3-1. 한 숫자의 리스트가 다른 알파를 만났을 때.(두 숫자가 같은 경우도 이에 해당됨.)
3-2. 서로 사이클에 다가가지 않고 베타끼리 만났을 때.  .... 요게 문제인데..
3-3. 서로 사이클에 도착하고 탐색했을 때 만났을 때
3-4. 서로 사이클에 도착했지만 사이클이 달랐을 때. ==> print(0), then pass

'''
######################################
'''
ex. 11 26을 넣었을 때... [11, 2, 4, 16], [26, 40, 16] --> 7.. 이경우 11,2,4 ~~ 4,16  ~~ 26,40,16 에 4,16에서는 -1. 
'''

'''  3-3 해결..
#endcycle 정의. 각각의 숫자 리스트가 서로 다른 사이클에 있는 숫자를 포함하고 있을 경우 print(-1)하고 pass.
cycle1 = [4,16,37,58,89,145,42,20]
cycle2 = [1]
print('a',cycle1.index(20))  #16,4,20 case를 생각해보자.. 반시계일때는 6, 시계일때는 2..
print('aa',cycle1.index(16)) 
alist = [11,2,4]
blist = [26,40,16]

cycle_dist = abs(cycle1.index(alist[-1])-cycle1.index(blist[-1]))
min( cycle_dist , 8 - cycle_dist ) 
#done.. cycle1에서 만났을 때 체크 성공.. 0~4까지 잘 리턴됨.
print('cycle_dist = ' , min( cycle_dist , 8 - cycle_dist ))  
absum = 0

absum += len(alist) + len(blist) + min( cycle_dist , 8 - cycle_dist )
print('bb',absum)
'''

 #잠깐 보류..
#endcycle 정의. 각각의 숫자 리스트가 서로 다른 사이클에 있는 숫자를 포함하고 있을 경우 print(0)하고 pass.
cycle1 = [4,16,37,58,89,145,42,20]
cycle2 = [1]

while True:
    a,b = map(int,input().strip().split())
    if (a==0) and (b==0):
        break
    
    alist = [a]
    blist = [b]
    while True: #alist 만들기.
        if (alist[-1] in cycle1) or (alist[-1] in cycle2):
            break
        
        square_sum = 0
        div_nbr = [int(i) for i in str(alist[-1])]
        for i in div_nbr:
            square_sum += i**2
        alist.append(square_sum)
        
        
    while True: #blist 만들기.
        if (blist[-1] in cycle1) or (blist[-1] in cycle2):
            break
        
        square_sum = 0
        div_nbr = [int(i) for i in str(blist[-1])]
        for i in div_nbr:
            square_sum += i**2
        blist.append(square_sum)  
    
    #list 변환과정.. done.
    
    # 프린트하는 과정! 첫번째, 세번째 clear..
    if (alist[0] in blist) or (blist[0] in alist):
        print(a,b,abs(len(blist) - len(alist))+2)  #시작하는 수가 다른 리스트에 그대로 들어가있는 경우.  done.
        
    elif (alist[-1]==1) and (blist[-1]==1):  #종착지가 둘 다 cycle2에 있는 경우.
        if len(set(alist)&set(blist))==1:  #1이 유일하게 겹치는 케이스. done.
            print(a,b,len(alist)+len(blist))   
        else: 
            while alist[-1] == blist[-1]:
                alist.remove(alist[-1])
                blist.remove(blist[-1])
            print(a,b,len(alist)+len(blist)+2)  #done.
            
    elif (alist[-1] in cycle1) and (blist[-1] in cycle1):   #종착지가 둘 다 cycle1에 있는 경우
        if alist[-1] != blist[-1]:  
            cycle_dist = abs(cycle1.index(alist[-1])-cycle1.index(blist[-1]))  
            #cycle1에서 a->b 방향 거리.(시계반시계 x)
            print(a,b,len(alist) + len(blist) + min( cycle_dist , 8 - cycle_dist )) 
            #cycle1으로 도착하는 종착지가 다름. done.
        else: 
            while alist[-1] == blist[-1]:
                alist.remove(alist[-1])
                blist.remove(blist[-1])
            print(a,b,len(alist)+len(blist)+2)  #위의 (*)와 같은 케이스. done.
            
    else:
        print(a,b,0) #만나지 않기 때문에 0을 리턴.
