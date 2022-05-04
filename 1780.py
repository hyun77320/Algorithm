# from os import sep
# n = int(input())

# paper = []
# for i in range(n):
#     paper.append(list(map(int, input().split())))


# solve(0,0,n)



# def solve(x,y,n):
#     isSame = bool(True)
#     for i in range(x+n):
#         for j in range(y+n):
#             paper[x][y] != paper[i][j]
#             isSame = 0 
#             break

    
#     if isSame:
#         if paper[x][y] == 1:
#             count1 ++
#         elif paper[x][y] == 0:
#             count0 ++
#         elif paper[x][y] == -1:
#             count-1 ++

#     else
#         m = n / 3

#         solve(x,y,m)
#         solve(x, y+m, m)
