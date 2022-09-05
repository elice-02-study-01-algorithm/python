def main():
    numNum = int(input())
    inputNum = list(map(int, input().split()))
    answer = 0
    for i in range(numNum):
        
        if (i+1)%2==0:
            
            if inputNum[i]%2==0:
                answer += inputNum[i]
    print(answer)
if __name__=="__main__":
    main()