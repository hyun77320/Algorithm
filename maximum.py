n = list(map(int, input().split()))
max = n[0]
l = 0

for i in range(1, len(n)):
    if max < n[i]:
        max = n[i]
        l = i + 1

print(max, l, end='\n')