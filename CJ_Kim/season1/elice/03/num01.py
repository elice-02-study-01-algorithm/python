sharp010 = '--#--'
sharp100 = '-#---'
sharp001 = '---#-'
sharp101 = '-#-#-'
sharp111 = '-###-'

num0 = [sharp111, sharp101, sharp101, sharp101, sharp111]
num1 = [sharp010, sharp010, sharp010, sharp010, sharp010]
num2 = [sharp111, sharp001, sharp111, sharp100, sharp111]
num3 = [sharp111, sharp001, sharp111, sharp001, sharp111]
num4 = [sharp101, sharp101, sharp111, sharp001, sharp001]
num5 = [sharp111, sharp100, sharp111, sharp001, sharp111]
num6 = [sharp111, sharp100, sharp111, sharp101, sharp111]
num7 = [sharp111, sharp101, sharp101, sharp001, sharp001]
num8 = [sharp111, sharp101, sharp111, sharp101, sharp111]
num9 = [sharp111, sharp101, sharp111, sharp001, sharp111]

def main():
    x = input()
    boardList = []
    for inputStr in x:
        if inputStr == '0':
            boardList.append(num0)
        elif inputStr == '1':
            boardList.append(num1)
        elif inputStr == '2':
            boardList.append(num2)
        elif inputStr == '3':
            boardList.append(num3)
        elif inputStr == '4':
            boardList.append(num4)
        elif inputStr == '5':
            boardList.append(num5)
        elif inputStr == '6':
            boardList.append(num6)
        elif inputStr == '7':
            boardList.append(num7)
        elif inputStr == '8':
            boardList.append(num8)
        elif inputStr == '9':
            boardList.append(num9)
    
    for i in range(5):
        lineStr = ''
        for j in boardList:
            lineStr += j[i]
            
        print(lineStr, sep='')
                

if __name__=="__main__":
    main()