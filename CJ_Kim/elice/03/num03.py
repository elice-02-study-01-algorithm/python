# 첫 두 케이스만 정답 처리, 이후에는 오답
# 왜 그런지 모르겠음

def main():
    dotNum = int(input())
    dotList = []
    for _ in range(dotNum):
        dot = list(map(int, input().split()))
        dotList.append(dot)
        
    answer = 0
    if dotNum < 3:
        print(0)
        exit()
    
    for i in range(dotNum-2):
        for j in range(1, dotNum-1):
            for k in range(2, dotNum):
                lineL1 = ((dotList[i][0]-dotList[j][0])**2+(dotList[i][1]-dotList[j][1])**2)**(1/2)
                lineL2 = ((dotList[k][0]-dotList[j][0])**2+(dotList[k][1]-dotList[j][1])**2)**(1/2)
                lineL3 = ((dotList[i][0]-dotList[k][0])**2+(dotList[i][1]-dotList[k][1])**2)**(1/2)
                lineLenList = [round(lineL1, 5), round(lineL2, 5), round(lineL3, 5)]
                lineLenList.sort()
                if lineLenList[0]+lineLenList[1] > lineLenList[2]:
                    answer += 1
    print(answer)
if __name__=="__main__":
    main()