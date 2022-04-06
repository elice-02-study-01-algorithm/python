import random
memList = ['관호', '채정', '송희', '형준', '지우', '재익']
random.shuffle(memList)
for i in range(len(memList)):
    
    print(memList[i], '->', memList[(i+1)%6])