n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = [0, 0]
for i in range(n):
    if a[i] == b[i]:
        answer[0] +=  1
    elif a[i] in b:
        answer[1] +=  1
print(answer[0], answer[1], sep="\n")