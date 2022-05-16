from sys import stdin

n = int(stdin.readline().strip())
a,b = list(map(int,stdin.readline().strip().split()))
m = int(stdin.readline().strip())
root_dict = {}

for i in range(m):
    par,chi = map(int,stdin.readline().strip().split())
    if par in root_dict.keys():
        root_dict[par].append(chi)
    else:
        root_dict[par] = [chi]

# print(root_dict)

def search_met(a,b,root_dict):
    a_anc = [a]
    b_anc = [b]
    
    while a_anc[-1] in sum(root_dict.values(),[]):
        for i in root_dict.keys():
            if a_anc[-1] in root_dict[i]:
                a_anc.append(i)
                break
            
    while b_anc[-1] in sum(root_dict.values(),[]):
        for i in root_dict.keys():
            if b_anc[-1] in root_dict[i]:
                b_anc.append(i)
                break
    
    # print(a_anc,b_anc)

    if len(set(a_anc) & set(b_anc)) == 0:
        return -1
    else:
        for i in a_anc:
            if i in b_anc:
                return a_anc.index(i) + b_anc.index(i)
    
print(search_met(a,b,root_dict))