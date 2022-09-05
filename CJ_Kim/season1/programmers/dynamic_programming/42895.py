# T(n) = T(n-N) + 1 또는 T(n+N) + 1 또는 T(n*N) + 1 또는 T(n/N)으로 점화식을 구하려 함
# T(n*N)의 경우를 따지자면 더 이상 점화식이 아니게 됨

# number = 1 ~ 5로 규칙을 찾으려 함
# 규칙따윈 없었음

# N()N()N()N 로 생각하여 각 빈 칸에 (연산자 없음), +, -, *, / 가 들어가는 경우를 생각해 봄
# 그래서 전부 연산한 걸 합집합 시키고 하나씩 추가하는 걸 생각해 봄
# 사실 정답이랑 그나마 가까웠지만 NNNNN = ([NNN]으로 연산한 것) + ([NN]으로 연산한 것)의 경우를 생각치 못함

# 정답은 어찌보면 브루트포스 알고리즘에 가깝지 않나...

# 참고 링크: https://gurumee92.tistory.com/164

def solution(N, number):
    
    # 1이 나오는 유일한 경우
    if N==number:
        return 1
    
    ansList = [ set() for _ in range(8)]
    
    
    for i, x in enumerate(ansList, start=1):
        x.add(int(str(N)*i))
    # ex. [{5}, {55}, {555}, {5555}, {55555}, {555555}, {5555555}, {55555555}]
    
    # 총 크기가 N으로 정해져 있고, i와 N-i의 연산이 각각 필요할 때 아래처럼 range쓰기 
    for i in range(1, 8):
        for j in range(i):
            # 집합 S(j개로 연산한 것들)
            for ope1 in ansList[j]:
                # 집합 S(i-j-1개로 연산한 것들)
                for ope2 in ansList[i-j-1]:
                    # 연산한 것들 모두 합집합시키기
                    ansList[i].add(ope1+ope2)
                    ansList[i].add(ope1-ope2)
                    ansList[i].add(ope1*ope2)
                    if ope2 != 0:
                        ansList[i].add(ope1//ope2)
        # 최솟값을 구해야 하고, 최소부터 계산을 하면서 계산값들을 구하고 있으니
        # for문 내에 if으로 그때그때 구하고 탈출시키는 방법
        if number in ansList[i]:
            answer = i+1
            break
        else:
            answer = -1
            
    return answer