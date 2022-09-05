from sys import stdin

def ascending(tpl,idx):
    for i in range(0,idx-1):
        if tpl[i]>tpl[i+1]:
            return False
    
    return True

def descending(tpl,idx):
    for i in range(idx,len(tpl)-1):
        if tpl[i]<tpl[i+1]:
            return False

    return True

def main():
    cases = int(stdin.readline().strip())

    for _ in range(cases):
        num = stdin.readline().strip()
        floor = tuple(map(int,stdin.readline().strip().split()))

        idx = floor.index(max(floor))

        if ascending(floor,idx) and descending(floor,idx):
            print('Yes')
        else:
            print('No')

if __name__=="__main__":
    main()