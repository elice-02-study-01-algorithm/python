import sys
input = sys.stdin.readline

testCase = int(input())

# 옷장의 든 종류별 옷 개수에다가 안 입는 경우를 합친 경우의 수
# 종류별로 위의 경우의 수를 곱한 뒤
# 마지막에 모두 안 입는 경우를 빼면 된다
def countCase(closet):
    if closet == {}:
        return 0
    case = 1
    for names in closet.values():
        case *= len(names)+1
    return case -1

for _ in range(testCase):
    closet = {}
    wearNum = int(input())
    for _ in range(wearNum):
        name, type = input().strip().split()
        if type in closet.keys():
            closet[type].append(name)
        else:
            closet[type]=[name]
    print(countCase(closet))
