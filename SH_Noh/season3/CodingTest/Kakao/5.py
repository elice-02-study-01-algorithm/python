# class Merge:
#     def __init__(self, index, data, merged = None):  # data만 입력시 next 초기값은 None이다.
#         self.index = index
#         self.data = data # 다음 데이터 주소 초기값 = None
#         self.merged = merged
from collections import defaultdict

def solution(commands):
    answer = []
    table = [[0] * 51 for _ in range(51)]
    merge_dict = defaultdict(list)
    notEmpty = []
    for command in commands:
        comm = command.split()
        if comm[0] == "UPDATE":
            if len(comm) == 4: # 1번 경우
                r, c, value = int(comm[1]), int(comm[2]), comm[3]
                if (r, c) in merge_dict:
                    for mr, mc in merge_dict[(r, c)]:
                        table[mr][mc] = value
                table[r][c] = value
                notEmpty.append((r, c))
            else: # 2번 경우, 있으면 다 바꿈
                value1, value2 = comm[1], comm[2]
                for r, c in notEmpty:
                    if table[r][c] == value1:
                        table[r][c] = value2

        if comm[0] == "MERGE": # 3번 경우
        # bfs 써야할 듯...
            r1, c1, r2, c2 = int(comm[1]), int(comm[2]), int(comm[3]), int(comm[4])
            # (r1, c1)에 값이 있는데 (r2, c2)가 병합된 셀이면 연결된 셀 모두 변경
            if table[r1][c1] != 0:
                if (r2, c2) in merge_dict:
                    for mr, mc in merge_dict[(r2, c2)]:
                        table[mr][mc] = table[r1][c1]
                else:
                    table[r2][c2] = table[r1][c1]
            elif table[r2][c2] != 0:
                if (r1, c1) in merge_dict:
                    for mr, mc in merge_dict[(r1, c1)]:
                        table[mr][mc] = table[r2][c2]
                else:
                    table[r1][c1] = table[r2][c2]
            merge_dict[(r1, c1)].append((r2, c2))
            merge_dict[(r2, c2)].append((r1, c1))

        if comm[0] == "UNMERGE": # 4번 경우
            r, c = int(comm[1]), int(comm[2])            
            # (r, c)가 병합된 상태면 연결된 셀의 값을 0으로 초기화, dict에서 삭제하고 반복
            for mr, mc in merge_dict[(r, c)]:
                table[mr][mc] = 0
                del merge_dict[(mr, mc)]
            del merge_dict[(r, c)]

        if comm[0] == "PRINT": # 5번 경우
            answer.append("EMPTY" if table[r][c] == 0 else table[r][c])

        print(comm)
        print(table[1], table[2])
        print(merge_dict)
        print("=======")

    return answer