from sys import stdin

N = int(stdin.readline())
papers = []
for _ in range(N):
    papers.append(stdin.readline().strip().split())

white = 0
blue = 0

def isCompleted(piece): # 완성형 색종이인가
    pieceSet = set() # set() 자료형 이용
    for i in range(len(piece)):
        pieceSet.update(piece[i]) # 모든 줄 넣어주기
    if len(pieceSet) == 1: # 모두 한 색상이면
        return True
    else: # 섞여있으면
        return False

def cutting(N, papers): # 색종이 자르기
    pieces = []
    global white, blue

    if isCompleted(papers): # 완성형 색종이이면
        if papers[0][0] == '0':
            white += 1
        else:
            blue += 1

    else:
        mid = N // 2
        # 각 조각들을 []로 묶어 왼>오 순서대로 pieces에 추가
        pieces.append([papers[i][:mid] for i in range(mid)])
        pieces.append([papers[i][mid:] for i in range(mid)])
        pieces.append([papers[mid+i][:mid] for i in range(mid)])
        pieces.append([papers[mid+i][mid:] for i in range(mid)])
        
        for j in range(4): # 항상 네 조각으로 나뉨
            # print(f'pieces[{j}]: {pieces[j]}')
            if isCompleted(pieces[j]): # 다 같은 색이면
                if pieces[j][0][0] == '0': # 색종이가 모두 흰색이면
                    white += 1
                else: # 파란색이면
                    blue += 1
            else: # 섞여있으면
                cutting(mid, pieces[j])

cutting(N, papers)
print(white)
print(blue)