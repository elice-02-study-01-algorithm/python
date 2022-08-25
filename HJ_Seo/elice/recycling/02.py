from sys import stdin

def main():
    x = stdin.readline().strip()
    
    arr1 = '-###- --#-- -###- -###- -#-#- -###- -###- -###- -###- -###-'.split()
    arr2 = '-#-#- --#-- ---#- ---#- -#-#- -#--- -#--- -#-#- -#-#- -#-#-'.split()
    arr3 = '-#-#- --#-- -###- -###- -###- -###- -###- -#-#- -###- -###-'.split()
    arr4 = '-#-#- --#-- -#--- ---#- ---#- ---#- -#-#- ---#- -#-#- ---#-'.split()
    arr5 = '-###- --#-- -###- -###- ---#- -###- -###- ---#- -###- -###-'.split()

    for i in x:
        print(arr1[int(i)],end='')
    print()
    for i in x:
        print(arr2[int(i)],end='')
    print()
    for i in x:
        print(arr3[int(i)],end='')
    print()
    for i in x:
        print(arr4[int(i)],end='')
    print()
    for i in x:
        print(arr5[int(i)],end='')
    print()
    
if __name__=="__main__":
    main()