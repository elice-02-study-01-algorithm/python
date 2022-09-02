# 전체적으로 봤을 때 가장 외곽에 있는 당근에서 
# +2를 한 것이 울타리 한 변의 길이가 됨
# 반복문으로 비교하면서 최소x값, 최대x값, 최소y값, 최대y값을 각각 구한다
def main():
    m, n, carrot = map(int, input().split())
    carrotMap = []
    for _ in range(carrot):
        x, y = map(int, input().split())
        carrotMap.append((x, y))
    
    maxM = 0
    minM = m
    maxN = 0
    minN = n
    for x, y in carrotMap:
        if x>maxM:
            maxM=x
        if x<minM:
            minM=x
        if y>maxN:
            maxN=y
        if y<minN:
            minN=y
    print(((maxM-minM+2)+(maxN-minN+2))*2)

if __name__=="__main__":
    main()