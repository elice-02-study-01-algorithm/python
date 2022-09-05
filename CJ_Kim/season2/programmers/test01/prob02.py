'''
want: 정현이가 사고 싶은 물품의 목록
number: 정현이가 사고 싶은 물품의 수
정현이는 want[i]를 number[i]개만큼 사고자 함

discount: 마트에서 매일 할인하는 물품의 목록 리스트

정현이는 열흘 간 물품을 사려고 하고, 해당 열흘 안에 자신이 원하는 만큼의 쇼핑을 하고자 한다.

정현이가 쇼핑을 할 수 있는 일수?
'''

'''
삼중 for문이어서 시간 초과날 줄 알았으나 100점!
'''
def solution(want, number, discount):
    # 열흘 안에 정현이가 쇼핑을 완전히 할 수 있는지 T/F로 반환
    def is_this_in(want, number, discount_list):
        count = 0
        for i in discount_list:
            if count == number:
                return True
            if i == want:
                count += 1
        if count == number:
            return True
        return False
    
    # 총 discount 리스트에서 열흘이 얼만큼 나올 수 있는지
    signin_index_limit = len(discount)-10
    answer = 0

    # 총 discount 리스트에서 10개씩 끊어서 검사하기
    for i in range(signin_index_limit+1):
        correct_count = 0
        for index in range(len(want)):
            if is_this_in(want[index], number[index], discount[i:i+10])==True:
                correct_count += 1
        if correct_count == len(want):
            answer += 1
    
    return answer

# test case



