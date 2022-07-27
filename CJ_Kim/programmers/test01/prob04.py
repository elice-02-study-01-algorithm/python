'''
체커 뒤집기

beginning에서 target으로 만들기 위해 뒤집어야 하는 최소 횟수
만들 수 없다면 -1
'''
'''
100점 만점 중 65점 맞았습니다.
핵심은 어떤 행이나 열이든 한 번만 뒤집는 것이 의미가 있지, 두세 번 뒤집는 것은 의미가 없다는 것.
따라서 beginning과 target을 비교하여 같은 부분, 다른 부분을 구별하고,
다른 부분을 같게 한 번씩 뒤집어 주는 것을 구현하면 됩니다.

그렇게 만든 행렬에서 한 행을 잡고 다른 부분을 찾아서 뒤집는데, 해당 열에 모든 체커들을 같이 뒤집습니다.
그런 다음 다음 행으로 넘어가서 [다른, 다른, ..., 다른] 일 경우 뒤집는 count를 올리고,
[같은, 같은, ..., 같은]일 경우 넘어가고,
그 이외의 경우에는 아무리 뒤집어도 target으로 만들 수 없는 경우로 분리합니다.

이 방식을 한 열을 잡고 다시 하여 둘 중 min값을 출력하면 됩니다.
(실제 모의고사 때는 이 부분을 생각하지 못해서 아마 100점을 못 맞은 것 같습니다.)
'''
def solution(beginning, target):

    row = len(beginning)

    # target과 beginning이 같으면 0, 다르면 1인 행렬 두 개 만들기
    even_or_odd_listR = [[] for _ in range(row)]
    even_or_odd_listC = [[] for _ in range(row)]
    for i in range(row):
        for j in range(row):
            if beginning[i][j] == target[i][j]:
                even_or_odd_listR[i].append(0)
                even_or_odd_listC[i].append(0)
            else:
                even_or_odd_listR[i].append(1)
                even_or_odd_listC[i].append(1)

    # 첫번째 case의 경우 다음과 같이 나옵니다.
    '''
    0 1 0 1 1
    1 0 1 0 0 
    0 1 0 1 1
    1 0 1 0 0
    0 1 0 1 1
    '''
    
    # 첫 행을 먼저 탐색하고 그 다음 행들 보기
    def startWithRow(even_or_odd_list):
        answer = 0

        for i in range(row):
            # 첫 행 중 원소가 1인 경우 해당 열의 모든 수를 뒤집어 줍니다.
            if even_or_odd_list[0][i] == 1:
                for j in range(1, row):
                    if even_or_odd_list[j][i] == 1:
                        even_or_odd_list[j][i] = 0
                    else:
                        even_or_odd_list[j][i] = 1
                # 뒤집을 때마다 횟수 증가
                answer += 1
        # 첫 행을 기준으로 뒤집은 것을 바탕으로 다음 행들을 검사합니다.
        for i in range(1, row):
            # [0, 0, ..., 0]인 경우 더 이상 뒤집을 필요가 없습니다.
            if even_or_odd_list[i] == [0 for _ in range(row)]:
                continue
            # [1, 1, ..., 1]인 경우 한 번 뒤집어 줘야 합니다.
            elif 1<= even_or_odd_list[i].count(1) < row:
                answer = -1
                break
            # 그 외의 경우 어떻게 뒤집든 target을 내놓을 수 없습니다.
            else:
                answer += 1
        return answer

    # 첫 열을 먼저 탐색하고 그 다음 열들 보기, startWithRow()와 거의 동일합니다.
    def startWithCol(even_or_odd_list):
        answer = 0
        for i in range(row):
            if even_or_odd_list[i][0] == 1:
                for j in range(1, row):
                    if even_or_odd_list[i][j] == 1:
                        even_or_odd_list[i][j] = 0
                    else:
                        even_or_odd_list[i][j] = 1
                answer += 1
        for i in range(1, row):
            col_list = [even_or_odd_list[j][i] for j in range(row)]
            if col_list == [0 for _ in range(row)]:
                continue
            elif 1<= col_list.count(1) < row:
                answer = -1
                break
            else:
                answer += 1
        return answer
    
    return min(startWithRow(even_or_odd_listR), startWithCol(even_or_odd_listC))

beginning01 = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
target01 = [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
beginning02 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
target02 = [[1, 0, 1], [0, 0, 0], [0, 0, 0]]
beginning03 = [[1, 1, 0, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]
target03 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
print(solution(beginning01, target01)) # 5
print(solution(beginning02, target02)) # -1
print(solution(beginning03, target03)) # 2
