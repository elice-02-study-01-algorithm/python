from sys import stdin

while True:
    try:
        cases = set()
        n = int(stdin.readline().rstrip())
        for _ in range(n):
            user = stdin.readline().rstrip()
            case = set()
            for i in user:
                if i not in case:
                    case.add(int(i))
            
            cases.add(tuple(case))
            
        print(len(cases))
        
    except:
        break

# ! ??????????? 이거 왜틀리나??...

# cases = set()
# n = int(stdin.readline().rstrip())
# for _ in range(n):
#     user = stdin.readline().rstrip()
#     case = set()
#     for i in user:
#         if i not in case:
#             case.add(int(i))
    
#     cases.add(tuple(case))
    
# print(len(cases))
# print(cases)