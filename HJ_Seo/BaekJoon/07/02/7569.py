from sys import stdin

def check_in_box(i,j,k):
    return
#     if i == 0:
#         if j == 0:
#             if k == 0:
#                 return ((1,0,0),(0,1,0),(0,0,1))
#             elif k == H-1:
#                 return ((1,0,H-1),(0,1,H-1),(0,0,H-2))
#             else:
#                 return ((1,0,k),(0,1,k),(0,0,k-1),(0,0,k+1))
#         elif j == N-1:
#             if k == 0:
#                 return ((1,N-1,0),(0,N-2,0),(0,N-1,1))
#             elif k == H-1:
#                 return ((1,N-1,H-1),(0,N-2,H-1),(0,N-1,H-2))
#             else:
#                 return ((1,N-1,k),(1,N-2,k),(0,N-1,k-1),(0,N-1,k+1))
#         else:
#             if k == 0:
#                 return ((1,j,0),(0,j-1,0),(0,j+1,0),(0,j,1))
#             elif k == H-1:
#                 return ((1,j,H-1),(0,j-1,H-1),(0,j+1,H-1),(0,j,H-2))
#             else:
#                 return ((1,j,k),(0,j-1,k),(0,j+1,k),(0,j,k-1),(0,j,k+1))
#     elif i == M-1:
#         if j == 0:
#             if k == 0:
#                 return ((M-2,0,0),(M-1,1,0),(M-1,0,1))
#             elif k == H-1:
#                 return ((M-2,0,H-1),(M-1,1,H-1),(M-1,0,H-2))
#             else:
#                 return ((M-2,0,k),(M-1,1,k),(M-1,0,k-1),(M-1,0,k+1))
#         elif j == N-1:
#             if k == 0:
#                 return ((M-2,N-1,0),(M-1,N-2,0),(M-1,N-1,1))
#             elif k == H-1:
#                 return ((M-2,N-1,H-1),(M-1,N-2,H-1),(M-1,N-1,H-2))
#             else:
#                 return ((M-2,N-1,k),(M-1,N-2,k),(M-1,N-1,k-1),(M-1,N-1,k+1))
#         else:
#             if k == 0:
#                 return ((M-2,j,0),(M-1,j-1,0),(M-1,j+1,0),(M-1,j,1))
#             elif k == H-1:
#                 return ((M-2,j,H-1),(M-1,j-1,H-1),(M-1,j+1,H-1),(M-1,j,H-2))
#             else:
#                 return ((M-2,j,k),(M-1,j-1,k),(M-1,j+1,k),(M-1,j,k-1),(M-1,j,k+1))
#     else:
#         if j == 0:
#             if k == 0:
#                 return ((i-1,0,0),(i+1,0,0),(i,1,0),(i,0,1))
#             elif k == H-1:
#                 return ((i-1,0,H-1),(i+1,0,H-1),(i,1,H-1),(i,0,H-2))
#             else:
#                 return ((i-1,0,k),(i+1,0,k),(i,1,k),(i,0,k-1),(i,0,k+1))
#         elif j == N-1:
#             if k == 0:
#                 return ((i-1,N-1,0),(i+1,N-1,0),(i,N-2,0),(i,N-1,1))
#             elif k == H-1:
#                 return ((i-1,N-1,H-1),(i+1,N-1,H-1),(i,N-2,H-1),(i,N-1,H-2))
#             else:
#                 return ((i-1,N-1,k),(i+1,N-1,k),(i,N-2,k),(i,N-1,k-1),(i,N-1,k+1))
#         else:
#             if k == 0:
#                 return ((i-1,j,0),(i+1,j,0),(i,j-1,0),(i,j+1,0),(i,j,1))
#             elif k == H-1:
#                 return ((i-1,j,H-1),(i+1,j,H-1),(i,j-1,H-1),(i,j+1,H-1),(i,j,H-2))
#             else:
#                 return ((i-1,j,k),(i+1,j,k),(i,j-1,k),(i,j+1,k),(i,j,k-1),(i,j,k+1))

def change_red():
    for i in range(M):
        for j in range(N):
            for k in range(H):
                
                if td[k][j][i] == 1:
                    change_num = check_in_box(i,j,k)    # ! inital code????????? ?????? ???????????? ????????????...
                    for w in change_num:
                        print(w)
                        if td[w[2]][w[1]][w[0]] == 0:
                            td[w[2]][w[1]][w[0]] = 1

M,N,H = map(int,stdin.readline().strip().split())

td = [[list(map(int,stdin.readline().strip().split())) for _ in range(N)] for _ in range(H)]
tomato_num = 0
for i in td:
    tomato_num += i.count(0)
    tomato_num += i.count(1)


n = 0
while True:
    change_red()

    if sum(sum(td,[])) == tomato_num:
        print(n)
        break
    n += 1
    if n == N*M*H:
        print(-1)
        break

# 301??? ?????????????????? 0??? ??????????????? print(-1).