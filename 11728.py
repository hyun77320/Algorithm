al, bl = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []

i, j, k = 0, 0, 0

while i < al and j < bl:
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1
    k += 1

while i < al:
    c.append(a[i])
    k += 1
    i += 1

while j < bl:
    c.append(b[j])
    k += 1
    j += 1

print(*c, sep=' ')