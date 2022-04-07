from sys import stdin

N = int(stdin.readline())
papers = []
for _ in range(N):
    papers.append(stdin.readline().strip().split())

white = 0
blue = 0

def cutting(N, papers):
    pieces = []
    global white, blue

    paperSet = set()
    for i in range(N):
        paperSet.update(papers[i])
    if len(paperSet) == 1:
        if list(paperSet)[0] == '0': # 색종이가 모두 흰색이면
            white += 1
            return
        else: # 파란색이면
            blue += 1
            return

    mid = N // 2
	# 각 조각들을 []로 묶어 왼>오 순서대로 pieces에 추가
    pieces.append([papers[i][:mid] for i in range(mid)])
    pieces.append([papers[i][mid:] for i in range(mid)])
    pieces.append([papers[mid+i][:mid] for i in range(mid)])
    pieces.append([papers[mid+i][mid:] for i in range(mid)])
    
    for j in range(4): # 탐색, 항상 네 조각으로 나뉨
        pieceSet = set() # set() 자료형 이용
        for k in range(len(pieces[j])):
            pieceSet.update(pieces[j][k]) # 모든 줄 넣어주기

        if len(pieceSet) == 1: # 다 같은 색이면
            if list(pieceSet)[0] == '0': # 색종이가 모두 흰색이면
                white += 1
            else: # 파란색이면
                blue += 1
            
        else: # 다른 색이 섞여있으면
            cutting(mid, pieces[j])

cutting(N, papers)
print(white)
print(blue)