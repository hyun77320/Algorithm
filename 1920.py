# a = int(input())
# n = list(map(int, input().split()))

# b = int(input())
# m = list(map(int, input().split()))

# c = [0 for i in range(b)]

# for i in range(a):
#     for j in range(b):
#         if n[i] == m[j]:
#             c[j] = 1

# print(*c, sep='\n')

N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
A.sort()

for num in arr:
    lt, rt = 0, N - 1		
    isExist = False		
    while lt <= rt:		
        mid = (lt + rt) // 2	
        if num == A[mid]:	
            isExist = True	
            print(1)		
            break		
        elif num > A[mid]:	
            lt = mid + 1	
        else:
            rt = mid - 1	

    if not isExist:		
        print(0)		