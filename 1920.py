a = int(input())
n = list(map(int, input().split()))

b = int(input())
m = list(map(int, input().split()))

c = [0 for i in range(b)]

for i in range(a):
    for j in range(b):
        if n[i] == m[j]:
            c[j] = 1

print(*c, sep='\n')