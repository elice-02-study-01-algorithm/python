# 문제 조건에 맞게 인덱스만 잘 설정해주면 된다
# 개인적인 느낌으로 '합'과 '최솟값, 최댓값'이라는 키워드가 나오면 브루트포스 알고리즘을 쓰는 것 같음
# 왼손의 범위와 오른손의 범위가 정해져있음
def main():
    N = int(input())
    goldList = list(map(int, input().split()))
    maxGold = 0
    for i in range(1, N-4):
        left = sum(goldList[i-1:i+2])
        for j in range(i+3, N-1):
            right = sum(goldList[j-1:j+2])
            if maxGold<(left+right):
                maxGold=left+right
                
    
    print(maxGold)

if __name__=="__main__":
    main()