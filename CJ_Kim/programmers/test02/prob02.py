'''
롤케이크에 올려진 토핑들의 번호를 저장한 정수 배열 topping이 매개변수로 주어질 때,
롤케이크를 공평하게 한 번 자르는 방법의 수를 return
공평하다: 각 조각 별 토핑의 가짓수가 같다.
'''
# 완전 탐색-시간 초과
'''
def solution(topping):
    answer = 0
    for i in range(len(topping)-1):
        chulSoo = topping[:i]
        dongsaeng = topping[i:]
        chulSooTopping = len(set(chulSoo))
        dongsaengTopping = len(set(dongsaeng))
        if chulSooTopping == dongsaengTopping:
            answer += 1

    return answer
'''
# 재귀-재귀 에러
'''
import sys
sys.setrecursionlimit(10000)
def solution(topping):
    
    def howMany(chul, dong):
        return len(set(chul)), len(set(dong))

    def slideRight(chul, dong):
        chul.append(dong.pop(0))
        return chul, dong

    def slideLeft(chul, dong):
        dong.insert(0, chul.pop())
        return chul, dong

    if len(set(topping))==1:
        return len(topping)-1
    mid = len(topping)//2
    curChul = topping[:mid]
    curDong = topping[mid:]
    
    global answer
    answer = 0

    def countFair(chul, dong):
        global answer

        a, b = howMany(chul, dong)
        if a == b:
            answer += 1
            countFair(*slideLeft(chul, dong))
            countFair(*slideRight(chul, dong))
        elif a > b:
            leftChul, leftDong = slideLeft(chul, dong)
            al, bl = howMany(leftChul, leftDong)
            if al<bl:
                return
            else:
                countFair(leftChul, leftDong)
        elif a < b:
            rightChul, rightDong = slideRight(chul, dong)
            ar, br = howMany(rightChul, rightDong)
            if ar>br:
                return
            else:
                countFair(rightChul, rightDong)

    countFair(curChul, curDong)

    return answer
'''
# 이분 탐색-25점
'''
def solution(topping):
    if len(set(topping))==1:
        return len(topping)-1

    def howMany(chul, dong):
        return len(set(chul)), len(set(dong))

    answer = 0

    start = 0
    end = len(topping)  - 1
    
    while True:
        if start > end:
            index = -1
            break
        index = (start+end) //2
        chulTop, dongTop = howMany(topping[:index], topping[index:])
        
        if chulTop < dongTop:
            start = index + 1
        elif chulTop > dongTop:
            end = index -1 
        else:
            break
        
    print('index', index)

    while True:
        index +=1
        chulTop, dongTop = howMany(topping[:index], topping[index:])
        if chulTop == dongTop:
            answer += 1
        else:
            break
    while True:
        index -=1
        chulTop, dongTop = howMany(topping[:index], topping[index:])
        if chulTop == dongTop:
            answer += 1
        else:
            break

    return answer
'''
# 이분 탐색=40점

def solution(topping):
    # 토핑이 한 가지일 경우 모든 조각으로 자르기
    if len(set(topping))==1:
        return len(topping)-1

    # 집합을 이용해서 각 롤케이크 조각마다 몇 가짓수가 있는지 세기
    def howMany(chul, dong):
        return len(set(chul)), len(set(dong))

    answer = 0

    # 이분 탐색
    start = 0
    end = len(topping)  - 1
    
    while True:
        if start > end:
            # 결국 같은 조건으로 걸린 인덱스가 없다면, 나눌 수 없다는 뜻이니
            index = -1
            break
        index = (start+end) //2
        chulTop, dongTop = howMany(topping[:index], topping[index:])
        
        # 만약 동생(오른쪽)조각의 가짓수가 많다면 인덱스를 오른쪽으로
        if chulTop < dongTop:
            start = index + 1
        # 만약 철수(왼쪽)조각의 가짓수가 많다면 인덱스를 왼쪽으로
        elif chulTop > dongTop:
            end = index -1 
        else:
            answer += 1
            break

    # 나눌 수 없는 경우
    if index == -1:
        return 0

    # 오른쪽으로 가면서 시험하는 경우
    toRightIndex = index
    # 왼쪽으로 가면서 시험하는 경우
    toLeftIndex = index

    # 오른쪽으로 한 칸씩 가면서 가짓수 비교하기
    while True:
        toRightIndex +=1
        # 만약 같은 수들의 나열일 경우, 세지 않고 그냥 오른쪽으로 옮기기
        # 가짓수가 동일함을 보장받았으므로
        if topping[toRightIndex] == topping[toRightIndex-1]:
            answer += 1
            continue
        else:
            # 가짓수 비교하기
            chulTop, dongTop = howMany(topping[:toRightIndex], topping[toRightIndex:])
            if chulTop == dongTop:
                answer += 1
            else:
                break
    
    # 왼쪽으로 한 칸씩 가면서 가짓수 비교하기
    while True:
        toLeftIndex -=1
        # 만약 같은 수들의 나열일 경우, 세지 않고 그냥 왼쪽으로 옮기기
        # 가짓수가 동일함을 보장받았으므로
        if topping[toLeftIndex] == topping[toLeftIndex+1]:
            answer += 1
            continue
        else:
            # 가짓수 비교하기
            chulTop, dongTop = howMany(topping[:toLeftIndex], topping[toLeftIndex:])
            if chulTop == dongTop:
                answer += 1
            else:
                break

    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2])) #2
print(solution([1, 2, 3, 1, 4])) #0

print(solution([1, 2, 3, 2, 2, 3])) #1