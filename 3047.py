n = list(map(int, input().split()))
abc = input()

for i in range(len(n) - 1, 0, -1):
        for j in range(i):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]

for i in abc:
    if i == 'A':
        print(n[0], end =' ')
    elif i == 'B':
        print(n[1], end =' ')
    elif i == 'C':
        print(n[2], end =' ')
