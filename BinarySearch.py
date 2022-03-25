from operator import index

target = int(input())
li = [1, 2, 3, 5, 7, 8, 9, 11, 15]
length = len(li)

L = 0
R = length-1

while L <= R:
    M = (L+R)//2
    if li[M] == target:
        print(M)
        break
    elif li[M] < target:
        L = M + 1
    else :
        R = M -1