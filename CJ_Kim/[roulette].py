import random
memList = ['관호', '채정', '송희', '형준', '지우', '재익']
random.shuffle(memList)
# 발표 순서
# print(memList)
# 코드 리뷰 매칭
for i in range(len(memList)):
    
    print(memList[i], '->', memList[(i+1)%6])