# https://www.acmicpc.net/board/view/73355
from itertools import product
from sys import stdin
input = stdin.readline

# 현재 100번에서 시작
# 먼저 제일 가까운 숫자를 찾아야 함
def main():
    channel_num = int(input())
    broken = int(input())
    length = len(str(channel_num))
    if broken == 0:
        print(min(length, abs(channel_num - 100)))
    else:
        # 일단 answer에 100번과의 차이를 저장
        answer = abs(channel_num - 100) if channel_num != 100 else 0

        broken_nums = set(input().split())
        nums = set(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])
        normal_nums = nums - broken_nums

        # 가능한 조합 중 원하는 채널보다 하나 작은 개수, 같은 개수, 하나 많은 개수의 길이인 경우 구하기
        possible_nums = []
        if length == 1:
            for x in range(length, length + 2):
                possible_nums.extend(product(normal_nums, repeat = x))
        else:
            for x in range(length - 1, length + 2):
                possible_nums.extend(product(normal_nums, repeat = x))

        for y in possible_nums:
            num = int("".join(y))
            if abs(channel_num - num) + len(y) < answer:
                answer = abs(channel_num - num) + len(y)
        print(answer)

main()