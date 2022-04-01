n = int(input())
re = []

for i in range(0, n):
    a, b = list(map(int, input().split()))
    re[i] = (a ** b) % 10
for j in range(0, n):
    print(re[j])

# for i in range(0, n):
#     print(re[i], end='/n')