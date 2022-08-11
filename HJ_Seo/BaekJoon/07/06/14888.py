'''
사칙연산을 할 수 있는 횟수가 차례대로 숫자로 주어졌기 때문에, 
연산을 할 첫 숫자와 뒤에 있는 숫자를 적절히 이용해서   
재귀함수 형식으로 함수를 짰습니다.

마지막으로 사칙연산의 횟수가 모두 0일 경우 
current에 남아있는 숫자는 모든 연산이 끝난 숫자가 되기 때문에 result에 더해주는 식으로 마무리를 짓고, 
원하는 출력값을 뽑아주게 했습니다.
'''

from sys import stdin

def calc_nums(current,lst,addi,subt,mult,divi):
    global result
    if addi == 0 and subt == 0 and mult == 0 and divi == 0:
        result += current
        return 
    
    num = lst[0]
    if addi != 0:
        new_current = [i+num for i in current]
        calc_nums(new_current,lst[1:],addi-1,subt,mult,divi)
    
    if subt != 0:
        new_current = [i-num for i in current]
        calc_nums(new_current,lst[1:],addi,subt-1,mult,divi)
        
    if mult != 0:
        new_current = [i*num for i in current]
        # print(new_current)
        calc_nums(new_current,lst[1:],addi,subt,mult-1,divi)
        
    if divi != 0:
        new_current = [i//num if i>0 else -((-i)//num) for i in current]
        calc_nums(new_current,lst[1:],addi,subt,mult,divi-1)
    
    return

n = input() #but 안씀.
nums = list(map(int,stdin.readline().strip().split()))

addi,subt,mult,divi = map(int,stdin.readline().strip().split())
current = []
initial = [nums[0]]
result = []
calc_nums(initial,nums[1:],addi,subt,mult,divi)

print(max(result))
print(min(result))
# print(result,max(result),min(result))