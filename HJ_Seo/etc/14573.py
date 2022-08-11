from sys import stdin

seq = [0,1,1]
sum_seq = [0,1,2]
num = 1000000007
init_num = 2
for i in range(3,1000001):
    nex = (seq[-1]*(2+init_num))%num
    sum_seq.append((sum_seq[-1]+nex)%num)
    seq.append(nex) # ! --> 요거 계산수가 문제인데..
    init_num = (init_num*2)%num
# print(seq[:15])
# print(sum_seq[:15])

case = int(stdin.readline().strip())

def sec_ord(numb):
    cnt = 0
    while True:
        if numb%2 != 0:
            return cnt # 이거도 업데이트가 가능할텐데... X --> at most O(16)
        
        numb = numb//2
        cnt += 1

for _ in range(case):
    
    arr = stdin.readline().strip()
    
    if arr.startswith('4'):
        order,one,i = map(int,arr.split())
        # if len(seq)-1 < i:
        #     for k in range(len(seq),i+1):
        #         seq.append((seq[-1]*(2+2**(k-2)))%num) # index update.
        
        print((one*seq[i])%num)
        continue
    
    order,one,i,j = map(int,arr.split())
    if i>j:
        i,j = j,i
    # if len(seq)-1 < max(i,j):
    #     for k in range(len(seq),max(i,j)+1):
    #         seq.append((seq[-1]*(2+2**(k-2)))%num) # index update.
            
    if order == 1: # a_i
        print((one*seq[i])%num)
        
    elif order == 2: #a_j를 2로 나눈 count
        # sec_ord(one*seq[max(i,j)])
        if j <=2:
            print(sec_ord(one)) # update1.. one을 2로 나눈 수에 각각의 init a_j들의 2의 지수들은 계산상 j-1와 동일.
        else:
            print(sec_ord(one)+(j-1)) # update2.. j가 1인 경우와 연산이 곱셈이 아닌 덧셈!!!
        
    elif order == 3:  # 이거 로직 맞는데...,,,,ㅠ
        print((one*(sum_seq[j] - sum_seq[i-1]))%num)
        # update2.. 여기도 one을 곱해줬어야했는데...,,,
        # print(sum(seq[i:j+1])%num) # 만약 줄인다면 이거...?

# ! 로직은 이게 맞는데... 좀 더 빠르게 쓸 방법은..?..   이게 틀렸다고??..