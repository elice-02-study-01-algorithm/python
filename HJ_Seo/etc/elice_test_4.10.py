def main():
    N,M,K = map(int,input().strip().split())
    total_needs_score = N*K
    lst = []
    nbr = 0 
    
    for i in range(N):
        grade,addi = map(int,input().strip().split())
        lst.append([M-grade,addi])
        total_needs_score -= grade
    
    # for i in lst:
    #     nbr+=i[0]*i[1]
    # case 5번과 case 9번의 답 체크코드.
    
    if total_needs_score<=0:
        return 0
    
    lst = sorted(lst,key = lambda x:x[1] )
    # total_needs_score 평균을 찍기 위해 필요한 점수.
    # lst 안에 있는 원소 i에 대하여 i[0]는 얻을 수 있는 점수, i[1]은 i에서 1점당 얻기 위해 필요한 과제량.
    # print(total_needs_score,lst)
    
    for i in lst:
        if total_needs_score>=i[0]:
            nbr += i[0]*i[1]
            total_needs_score -= i[0]
        elif total_needs_score<=i[0]:
            nbr += total_needs_score*i[1]
            return nbr
    print(nbr)
    return -1 # 원래 넣으려고 했던 것은 -1 혹은 '모든 과제를 해도 평균점수를 넘지 못했습니다.' 입니다.
    
if __name__=="__main__":
    print(main())
    
'''
100 62 62
58 60
56 70
46 90
43 54
55 20
56 58
36 4
57 74
38 31
35 72
35 68
40 48
1 4
39 95
17 78
53 28
60 53
40 51
39 13
49 49
60 98
59 38
20 99
12 54
59 89
40 38
35 27
31 75
31 12
37 3
34 80
4 30
50 33
52 85
54 78
34 73
55 47
47 52
39 46
36 49
25 74
49 76
52 12
58 29
23 81
27 18
2 87
4 70
33 4
61 57
55 49
59 67
50 81
54 20
9 91
61 45
33 99
2 29
46 77
36 26
11 17
28 22
31 48
47 50
60 38
5 94
58 45
15 8
62 81
17 98
8 88
21 31
15 76
53 97
17 91
22 30
37 9
53 43
61 25
46 83
38 61
36 74
2 53
5 72
27 97
44 9
28 23
39 68
11 87
36 80
7 87
35 76
46 17
16 39
4 52
12 27
26 94
2 4
8 33
58 45
'''
