n = int(input())

def noc(a):
    if a == 1:
        return 1
    elif a == 2:
        return 2
    elif a == 3:
        return 4
    else:
        return noc(a-1) + noc(a-2) + noc(a-3)

li = []

for i in range(n):
    a = int(input())
    li.append(noc(a))

print(*li, sep='\n')