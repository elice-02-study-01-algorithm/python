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