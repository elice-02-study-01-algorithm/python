from sys import stdin,maxsize

n = int(stdin.readline().strip())

pieces = list(map(int,stdin.readline().strip().split()))

m = int(stdin.readline().strip())
# ! m 이하로 짤라서 최대 - 최소...

'''
5
13 69 41 37 80
27
'''

# about_size = sum(pieces)/(m+n-1)
# # print(about_size)
# lst = [pieces[i]/about_size for i in range(n)]
# print(lst)

# lst = [[int(pieces[i]/about_size) for i in range(n)],[]]
# print(lst[0])

# def diff_min_max(n,lst,pieces):
#     x = pieces.copy()
#     for i in range(n):
#         x[i] = pieces[i]/lst[i]
#     return x


# x = diff_min_max(n,lst[0],pieces)
# print(x, max(x)-min(x))

'''
qq

'''
# while m != 0:
#     max_piece = max(pieces)
#     if pieces[max_piece] == 1:
#         del pieces[max_piece]
#     else:
#         pieces[max_piece] -= 1
    
#     if max_piece/2 not in pieces:
#         pieces[max_piece/2] = 0
#     pieces[max_piece/2] += 2
    
#     m -= 1

# print(pieces)
# print(max(pieces) - min(pieces))