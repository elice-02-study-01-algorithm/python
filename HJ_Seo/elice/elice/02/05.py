from sys import stdin

# N: 사람수, K:시작하는 사람.
N,K = map(int,stdin.readline().strip().split())

# peopl[i번 사람 index]: [i_left, i_right]
peopl = dict()

for i in range(1,N+1):
    peopl[i]=list(map(int,stdin.readline().strip().split()))

def bfs(discarded_num,current_discarded_num,peopl):
    current = []
    for i in range(len(current_discarded_num)):
        discarded_num.add(current_discarded_num[i])
        x = peopl[current_discarded_num[i]]
        # x_left가 선택된 케이스가 없을 때 current에 추가
        if x[0] not in discarded_num and x[0] not in current:
            # print('x[0] =',x[0])
            current.append(x[0])
        
        # 마찬가지로 x_right가 선택된 케이스가 없을 때 current에 추가
        if x[1] not in discarded_num and x[1] not in current:
            # print('x[1] =',x[1])
            current.append(x[1])
    
    return discarded_num,current
        

discarded_num = {K} #처음 술래로 선택된 사람.
current_discarded_num = peopl[K].copy() 

while len(current_discarded_num) != 0: #다음 구성요소가 없으면 stop..
    # print(discarded_num,current_discarded_num)
    discarded_num,current_discarded_num = bfs(discarded_num,current_discarded_num,peopl)

print(N-len(discarded_num))


# ! 살짝 맘에 들지 않는 코드이다.. current_discarded_num 에 대한 setting을 다시 할 필요가 있음. 